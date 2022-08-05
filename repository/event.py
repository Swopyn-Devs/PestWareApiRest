from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session

from fastapi_jwt_auth import AuthJWT
from pydantic import UUID4
from sqlalchemy.orm import Session

from models.event import Event
from schemas.event import EventRequest
from utils import folios

from utils.functions import *


model_name = 'evento'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, Event, authorize, paginate_param, True)


def retrieve(db: Session, event_id: UUID4):
    return get_data(db, Event, event_id, model_name)


def create(db: Session, request: EventRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = Event(
        title = request.title,
        folio = folios.event(db, employee.job_center_id, request.event_type_id),
        event_type_id = request.event_type_id,
        initial_date = request.initial_date,
        final_date = request.final_date,
        initial_hour = request.initial_hour,
        final_hour = request.final_hour,
        quote_id = request.quote_id,
        customer_id = request.customer_id,
        employee_id = request.employee_id,
        service_type_id = request.service_type_id,
        total = request.total,
        comments = request.comments,
        job_center_id = employee.job_center_id
    )
    last_id = insert_data(db, request_data)
    return get_data(db, Event, last_id, model_name)


def update(db: Session, request: EventRequest, model_id: UUID4):
    return update_data(db, Event, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, Event, model_id, model_name)