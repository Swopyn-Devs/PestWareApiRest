from utils import functions
from decouple import config
from fastapi import HTTPException, status, UploadFile
from fastapi_pagination import paginate, Params
from pydantic import UUID4
from slugify import slugify
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.job_center import JobCenter
from schemas.job_center import JobCenterRequest
from services import aws

model_name = 'centro de trabajo'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    data = functions.get_all_data(db, JobCenter, authorize, 'all', False)
    aux = 0
    for d in data:
        data[aux] = map_s3_url(d)
        aux += 1

    if paginate_param:
        return paginate(data)

    data_size = len(data)
    if data_size <= 0:
        data_size = 1
    return paginate(data, Params(size=data_size))


def retrieve(db: Session, job_center_id: UUID4):
    data = functions.get_data(db, JobCenter, job_center_id, model_name)
    return map_s3_url(data)


def create(db: Session, request: JobCenterRequest):
    slug = slugify(request.name)
    new_job_center = JobCenter(
        name=request.name,
        slug=slug,
        business_name=request.business_name,
        health_manager=request.health_manager,
        company_id=request.company_id,
        taxpayer_registration=request.taxpayer_registration,
        license_number=request.license_number,
        email=request.email,
        phone=request.phone,
        whatsapp=request.whatsapp,
        web_page=request.web_page,
        facebook=request.facebook,
        messenger=request.messenger,
        timezone=request.timezone
    )

    last_id = functions.insert_data(db, new_job_center)
    return functions.get_data(db, JobCenter, last_id, model_name)


def update(db: Session, request: JobCenterRequest, model_id: UUID4):
    return functions.update_data(db, JobCenter, model_id, model_name, request.dict())


def update_sanitary_license(db: Session, license_pdf: UploadFile, model_id: UUID4):
    validate_pdf(license_pdf)
    key = f'sanitary_licenses/{model_id}.pdf'
    data = functions.update_data(db, JobCenter, model_id, model_name, {'sanitary_license': key})

    # Upload file to AWS S3
    if not aws.upload_image(config('AWS_S3_BUCKET_COMPANIES'), key, license_pdf):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f'No fue posible actualizar el logo para documentos.')

    return map_s3_url(data)


def delete(db: Session, model_id: UUID4):
    return functions.update_delete(db, JobCenter, model_id, model_name)


def map_s3_url(job_center: JobCenter):
    if type(job_center) is dict:
        if job_center['sanitary_license'] is not None:
            job_center['sanitary_license'] = f"{config('AWS_S3_URL_COMPANIES')}/{job_center['sanitary_license']}"
    else:
        if job_center.sanitary_license is not None:
            job_center.sanitary_license = f"{config('AWS_S3_URL_COMPANIES')}/{job_center.sanitary_license}"

    return job_center


def validate_pdf(pdf):
    allowed_types = ['application/pdf']
    if pdf.content_type not in allowed_types:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='La licencia debe ser de tipo pdf: (.pdf).')
