from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.job_title import JobTitle
from schemas.job_title import JobTitleRequest, JobTitleUpdateRequest

model_name = 'puesto'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, JobTitle, authorize, paginate_param, True)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, JobTitle, model_id, model_name)


def create(db: Session, request: JobTitleRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = JobTitle(
        name=request.name,
        job_center_id=employee.job_center_id,
    )
    insert_data(db, request_data)
    return request_data


def update(db: Session, request: JobTitleUpdateRequest, model_id: UUID4):
    return update_data(db, JobTitle, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, JobTitle, model_id, model_name)
