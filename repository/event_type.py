from utils.functions import *
from decouple import config
from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
from models.event_type import EventType
from schemas.event_type import EventTypeRequest, EventTypeUpdateRequest


model_name = 'tipo de evento'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, EventType, authorize, paginate_param, True)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, EventType, model_id, model_name)


def create(db: Session, request: EventTypeRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = EventType(
        name = request.name,
        quote_field = request.quote_field,
        customer_field = request.customer_field,
        employee_field = request.employee_field,
        service_type_field = request.service_type_field,
        plagues_field =request.plagues_field,
        cost_field = request.cost_field,
        comments_field = request.comments_field,
        inspection_form = request.inspection_form,
        condition_form = request.condition_form,
        control_form = request.control_form,
        payment_form = request.payment_form,
        signature_form = request.signature_form,
        notification_action = request.notification_action,
        reminder_action = request.reminder_action,
        folio_key_setting = request.folio_key_setting,
        folio_init_setting = request.folio_init_setting,
        is_service_order = request.is_service_order,
        job_center_id = employee.job_center_id
    )
    last_id = insert_data(db, request_data)
    return get_data(db, EventType, last_id, model_name)


def update(db: Session, request: EventTypeUpdateRequest, model_id: UUID4):
    return update_data(db, EventType, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, EventType, model_id, model_name)