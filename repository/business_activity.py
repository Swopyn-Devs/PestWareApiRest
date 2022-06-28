from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.business_activity import BusinessActivity
from schemas.business_activity import BusinessActivityRequest, BusinessActivityUpdateRequest

model_name = 'giro de la empresa'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, BusinessActivity, authorize, paginate_param, True)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, BusinessActivity, model_id, model_name)


def create(db: Session, request: BusinessActivityRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = BusinessActivity(
        name=request.name,
        job_center_id=employee.job_center_id
    )
    last_id = insert_data(db, request_data)
    return get_data(db, BusinessActivity, last_id, model_name)


def update(db: Session, request: BusinessActivityUpdateRequest, model_id: UUID4):
    return update_data(db, BusinessActivity, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, BusinessActivity, model_id, model_name)
