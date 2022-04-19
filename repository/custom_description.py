from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.custom_description import CustomDescription
from schemas.custom_description import CustomDescriptionRequest, CustomDescriptionUpdateRequest

model_name = 'descripción personalizada'


def get_all(db: Session, authorize: AuthJWT):
    return get_all_data(db, CustomDescription, authorize)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, CustomDescription, model_id, model_name)


def create(db: Session, request: CustomDescriptionRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = CustomDescription(
        name=request.name,
        description=request.description,
        job_center_id=employee.job_center_id
    )
    insert_data(db, request_data)
    return request_data


def update(db: Session, request: CustomDescriptionUpdateRequest, model_id: UUID4):
    return update_data(db, CustomDescription, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, CustomDescription, model_id, model_name)
