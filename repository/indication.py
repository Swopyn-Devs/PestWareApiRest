from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.indication import Indication
from schemas.indication import IndicationRequest, IndicationUpdateRequest

model_name = 'indicación'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, Indication, authorize, paginate_param, True)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, Indication, model_id, model_name)


def create(db: Session, request: IndicationRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = Indication(
        name=request.name,
        key=request.key,
        description=request.description,
        job_center_id=employee.job_center_id
    )
    last_id = insert_data(db, request_data)
    return get_data(db, Indication, last_id, model_name)


def update(db: Session, request: IndicationUpdateRequest, model_id: UUID4):
    return update_data(db, Indication, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, Indication, model_id, model_name)
