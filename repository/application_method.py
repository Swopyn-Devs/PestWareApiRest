from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.application_method import ApplicationMethod
from schemas.application_method import ApplicationMethodRequest, ApplicationMethodUpdateRequest

model_name = 'método de aplicación'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, ApplicationMethod, authorize, paginate_param, True)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, ApplicationMethod, model_id, model_name)


def create(db: Session, request: ApplicationMethodRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = ApplicationMethod(
        name=request.name,
        job_center_id=employee.job_center_id,
    )
    last_id = insert_data(db, request_data)
    return get_data(db, ApplicationMethod, last_id, model_name)


def update(db: Session, request: ApplicationMethodUpdateRequest, model_id: UUID4):
    return update_data(db, ApplicationMethod, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, ApplicationMethod, model_id, model_name)
