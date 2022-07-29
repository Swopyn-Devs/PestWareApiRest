from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.event_type import EventType
from models.mip_condition_form import MIPConditionForm
from schemas.mip_condition_form import MIPConditionFormRequest

model_name = 'formulario de condición MIP'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, MIPConditionForm, authorize, paginate_param)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, MIPConditionForm, model_id, model_name)


def create(db: Session, request: MIPConditionFormRequest):
    get_data(db, EventType, request.event_id, 'tipo de evento')
    request_data = MIPConditionForm(
        event_id=request.event_id,
        indications=request.indications,
        restricted_access=request.restricted_access,
        comments=request.comments
    )
    last_id = insert_data(db, request_data)
    return get_data(db, MIPConditionForm, last_id, model_name)


def update(db: Session, request: MIPConditionFormRequest, model_id: UUID4):
    get_data(db, EventType, request.event_id, 'tipo de evento')
    return update_data(db, MIPConditionForm, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, MIPConditionForm, model_id, model_name)
