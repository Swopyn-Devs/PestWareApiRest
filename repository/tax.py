from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session

from models.tax import Tax
from schemas.tax import TaxRequest

model_name = 'impuesto'


def get_all(db: Session):
    return get_all_data(db, Tax)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, Tax, model_id, model_name)


def create(db: Session, request: TaxRequest):
    request_data = Tax(
        name=request.name,
        value=request.value,
        job_center_id=request.job_center_id
    )
    insert_data(db, request_data)
    return request_data


def update(db: Session, request: TaxRequest, model_id: UUID4):
    return update_data(db, Tax, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, Tax, model_id, model_name)
