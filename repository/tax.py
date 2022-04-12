from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.tax import Tax
from schemas.tax import TaxRequest, TaxUpdateRequest

model_name = 'impuesto'


def get_all(db: Session, authorize: AuthJWT):
    return get_all_data(db, Tax, authorize)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, Tax, model_id, model_name)


def create(db: Session, request: TaxRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = Tax(
        name=request.name,
        value=request.value,
        job_center_id=employee.job_center_id
    )
    insert_data(db, request_data)
    return request_data


def update(db: Session, request: TaxUpdateRequest, model_id: UUID4):
    return update_data(db, Tax, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, Tax, model_id, model_name)
