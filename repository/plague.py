from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.plague import Plague
from schemas.plague import PlagueRequest, PlagueUpdateRequest

model_name = 'plaga'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, Plague, authorize, paginate_param, True)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, Plague, model_id, model_name)


def create(db: Session, request: PlagueRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = Plague(
        name=request.name,
        plague_category_id=request.plague_category_id,
        job_center_id=employee.job_center_id
    )
    last_id = insert_data(db, request_data)
    return get_data(db, Plague, last_id, model_name)


def update(db: Session, request: PlagueUpdateRequest, model_id: UUID4):
    return update_data(db, Plague, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, Plague, model_id, model_name)
