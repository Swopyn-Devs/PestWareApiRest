from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.status import Status
from schemas.status import StatusRequest

model_name = 'estatus'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, Status, authorize, paginate_param, False)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, Status, model_id, model_name)


def create(db: Session, request: StatusRequest):
    request_data = Status(
        name=request.name,
        key_string=request.key_string,
        module=request.module
    )
    insert_data(db, request_data)
    return request_data


def update(db: Session, request: StatusRequest, model_id: UUID4):
    return update_data(db, Status, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, Status, model_id, model_name)
