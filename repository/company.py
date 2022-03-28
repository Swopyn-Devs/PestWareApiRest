from decouple import config
from fastapi import HTTPException, status, UploadFile
from pydantic import UUID4
from sqlalchemy.orm import Session

from models.company import Company
from schemas.company import CompanyRequest
from services import aws


def get_all(db: Session):
    companies = db.query(Company).all()
    data = []
    for company in companies:
        data.append(map_s3_url(company))

    return data


def retrieve(db: Session, company_id: UUID4):
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'La empresa con el id {company_id} no está disponible.')

    return map_s3_url(company)


def update(db: Session, request: CompanyRequest, company_id: UUID4):
    company = db.query(Company).filter(Company.id == company_id)
    if not company.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'La empresa con el id {company_id} no está disponible.')

    company.update(request.dict())
    db.commit()

    return company.first()


def update_document_logo(db: Session, logo: UploadFile, company_id: UUID4):
    company = db.query(Company).filter(Company.id == company_id)
    if not company.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'La empresa con el id {company_id} no está disponible.')

    validate_image(logo)

    # Upload file to AWS S3
    key = f'document_logos/{company_id}.jpeg'
    if not aws.upload_image(config('AWS_S3_BUCKET'), key, logo):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f'No fue posible actualizar el logo para documentos.')

    company.update({'document_logo': key})
    db.commit()

    return map_s3_url(company.first())


def update_document_stamp(db: Session, logo: UploadFile, company_id: UUID4):
    company = db.query(Company).filter(Company.id == company_id)
    if not company.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'La empresa con el id {company_id} no está disponible.')

    validate_image(logo)

    # Upload file to AWS S3
    key = f'document_stamps/{company_id}.jpeg'
    if not aws.upload_image(config('AWS_S3_BUCKET'), key, logo):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f'No fue posible actualizar el sello para documentos.')

    company.update({'document_stamp': key})
    db.commit()

    return map_s3_url(company.first())


def update_web_logo(db: Session, logo: UploadFile, company_id: UUID4):
    company = db.query(Company).filter(Company.id == company_id)
    if not company.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'La empresa con el id {company_id} no está disponible.')

    validate_image(logo)

    # Upload file to AWS S3
    key = f'web_logos/{company_id}.jpeg'
    if not aws.upload_image(config('AWS_S3_BUCKET'), key, logo):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f'No fue posible actualizar el logo para web.')

    company.update({'web_logo': key})
    db.commit()

    return map_s3_url(company.first())


def delete(db: Session, company_id: UUID4):
    company = db.query(Company).filter(Company.id == company_id)
    if not company.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'La empresa con el id {company_id} no está disponible.')

    company.update({'is_deleted': True})
    db.commit()

    return {'detail': 'La empresa se elimino correctamente.'}


def map_s3_url(company: Company):
    if company.document_logo is not None:
        company.document_logo = f"{config('AWS_S3_URL')}/{company.document_logo}"
    if company.document_stamp is not None:
        company.document_stamp = f"{config('AWS_S3_URL')}/{company.document_stamp}"
    if company.web_logo is not None:
        company.web_logo = f"{config('AWS_S3_URL')}/{company.web_logo}"

    return company


def validate_image(image):
    allowed_types = ['image/jpeg', 'image/jpg']
    if image.content_type not in allowed_types:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='El avatar debe ser de tipo imagen: (.jpg o .jpeg).')
