from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.presentation import Presentation
from schemas.presentation import PresentationRequest, PresentationUpdateRequest

model_name = 'presentación del producto'


def get_all(db: Session, authorize: AuthJWT):
    return get_all_data(db, Presentation, authorize)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, Presentation, model_id, model_name)


def create(db: Session, request: PresentationRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = Presentation(
        name=request.name,
        job_center_id=employee.job_center_id,
    )
    insert_data(db, request_data)
    return request_data


def update(db: Session, request: PresentationUpdateRequest, model_id: UUID4):
    return update_data(db, Presentation, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, Presentation, model_id, model_name)
