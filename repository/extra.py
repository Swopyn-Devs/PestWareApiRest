from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.extra import Extra
from schemas.extra import ExtraRequest, ExtraUpdateRequest

model_name = 'extra'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, Extra, authorize, paginate_param, True)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, Extra, model_id, model_name)


def create(db: Session, request: ExtraRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = Extra(
        name=request.name,
        description=request.description,
        quantity=request.quantity,
        job_center_id=employee.job_center_id
    )
    insert_data(db, request_data)
    return request_data


def update(db: Session, request: ExtraUpdateRequest, model_id: UUID4):
    return update_data(db, Extra, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, Extra, model_id, model_name)
