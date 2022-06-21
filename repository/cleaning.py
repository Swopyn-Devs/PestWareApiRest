from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.cleaning import Cleaning
from schemas.cleaning import CleaningRequest, CleaningUpdateRequest

model_name = 'orden y limpieza'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, Cleaning, authorize, paginate_param, True)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, Cleaning, model_id, model_name)


def create(db: Session, request: CleaningRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = Cleaning(
        name=request.name,
        job_center_id=employee.job_center_id,
    )
    last_id = insert_data(db, request_data)
    return get_data(db, Cleaning, last_id, model_name)


def update(db: Session, request: CleaningUpdateRequest, model_id: UUID4):
    return update_data(db, Cleaning, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, Cleaning, model_id, model_name)
