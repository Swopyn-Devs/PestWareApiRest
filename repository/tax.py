from utils.messages import *

from fastapi import HTTPException, status
from fastapi_pagination import paginate
from pydantic import UUID4
from sqlalchemy.orm import Session

from models.tax import Tax
from schemas.tax import TaxRequest

model_name = 'impuesto'

def get_all(db: Session):
    return paginate(db.query(Tax).all())


def retrieve(db: Session, model_id: UUID4):
    data = db.query(Tax).filter(Tax.id == model_id).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=detail_message(model_name, model_id))
    return data


def create(db: Session, request: TaxRequest):
    data = Tax(
        name=request.name,
        value=request.value,
        job_center_id=request.job_center_id,
    )
    db.add(data)
    db.commit()
    db.refresh(data)

    return data


def update(db: Session, request: TaxRequest, model_id: UUID4):
    data = db.query(Tax).filter(Tax.id == model_id)
    if not data.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=detail_message(model_name, model_id))

    data.update(request.dict())
    db.commit()

    return data.first()


def delete(db: Session, model_id: UUID4):
    data = db.query(Tax).filter(Tax.id == model_id)
    if not data.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=detail_message(model_name, model_id))

    data.update({'is_deleted': True})
    db.commit()

    return {'detail': delete_message(model_name)}
