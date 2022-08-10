from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.event import Event
from models.mip_inspection_form import MIPInspectionForm
from schemas.mip_inspection_form import MIPInspectionFormRequest

model_name = 'formulario de inspección MIP'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, MIPInspectionForm, authorize, paginate_param)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, MIPInspectionForm, model_id, model_name)


def create(db: Session, request: MIPInspectionFormRequest):
    get_data(db, Event, request.event_id, 'evento')
    request_data = MIPInspectionForm(
        event_id=request.event_id,
        nesting_areas=request.nesting_areas,
        comments=request.comments
    )
    last_id = insert_data(db, request_data)
    return get_data(db, MIPInspectionForm, last_id, model_name)


def update(db: Session, request: MIPInspectionFormRequest, model_id: UUID4):
    get_data(db, Event, request.event_id, 'evento')
    return update_data(db, MIPInspectionForm, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, MIPInspectionForm, model_id, model_name)
