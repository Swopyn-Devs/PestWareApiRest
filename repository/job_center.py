from decouple import config
from fastapi import HTTPException, status, UploadFile
from fastapi_pagination import paginate
from pydantic import UUID4
from slugify import slugify
from sqlalchemy.orm import Session

from models.job_center import JobCenter
from schemas.job_center import JobCenterRequest
from services import aws


def get_all(db: Session):
    job_centers = db.query(JobCenter).all()
    data = []
    for job_center in job_centers:
        data.append(map_s3_url(job_center))

    return paginate(data)


def retrieve(db: Session, job_center_id: UUID4):
    job_center = db.query(JobCenter).filter(JobCenter.id == job_center_id).first()
    if not job_center:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El centro de trabajo con el id {job_center_id} no está disponible.')

    return map_s3_url(job_center)


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
    db.add(new_job_center)
    db.commit()
    db.refresh(new_job_center)

    return new_job_center


def update(db: Session, request: JobCenterRequest, job_center_id: UUID4):
    job_center = db.query(JobCenter).filter(JobCenter.id == job_center_id)
    if not job_center.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El centro de trabajo con el id {job_center_id} no está disponible.')

    job_center.update(request.dict())
    db.commit()

    return job_center.first()


def update_sanitary_license(db: Session, license_pdf: UploadFile, job_center_id: UUID4):
    job_center = db.query(JobCenter).filter(JobCenter.id == job_center_id)
    if not job_center.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El centro de trabajo con el id {job_center_id} no está disponible.')

    validate_pdf(license_pdf)

    # Upload file to AWS S3
    key = f'sanitary_licenses/{job_center_id}.pdf'
    if not aws.upload_image(config('AWS_S3_BUCKET_COMPANIES'), key, license_pdf):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f'No fue posible actualizar el logo para documentos.')

    job_center.update({'sanitary_license': key})
    db.commit()

    return map_s3_url(job_center.first())


def delete(db: Session, job_center_id: UUID4):
    job_center = db.query(JobCenter).filter(JobCenter.id == job_center_id)
    if not job_center.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El centro de trabajo con el id {job_center_id} no está disponible.')

    job_center.update({'is_deleted': True})
    db.commit()

    return {'detail': 'El centro de trabajo se elimino correctamente.'}


def map_s3_url(job_center: JobCenter):
    if job_center.sanitary_license is not None:
        job_center.sanitary_license = f"{config('AWS_S3_URL_COMPANIES')}/{job_center.sanitary_license}"

    return job_center


def validate_pdf(pdf):
    allowed_types = ['application/pdf']
    if pdf.content_type not in allowed_types:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='La licencia debe ser de tipo pdf: (.pdf).')
