from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.event import Event
from models.payment_method import PaymentMethod
from models.payment_way import PaymentWay
from models.status import Status
from models.mip_payment_form import MIPPaymentForm
from schemas.mip_payment_form import MIPPaymentFormRequest

model_name = 'formulario de pago MIP'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, MIPPaymentForm, authorize, paginate_param)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, MIPPaymentForm, model_id, model_name)


def create(db: Session, request: MIPPaymentFormRequest):
    get_data(db, Event, request.event_id, 'evento')
    get_data(db, PaymentMethod, request.payment_method_id, 'método de pago')
    get_data(db, PaymentWay, request.payment_way_id, 'forma de pago')

    status_id = get_status_id()
    if request.status_id is not None:
        get_data(db, Status, request.status_id, 'estatus')
        status_id = request.status_id

    request_data = MIPPaymentForm(
        event_id=request.event_id,
        payment_method_id=request.payment_method_id,
        payment_way_id=request.payment_way_id,
        amount=request.amount,
        status_id=status_id
    )
    last_id = insert_data(db, request_data)
    return get_data(db, MIPPaymentForm, last_id, model_name)


def update(db: Session, request: MIPPaymentFormRequest, model_id: UUID4):
    get_data(db, Event, request.event_id, 'evento')
    get_data(db, PaymentMethod, request.payment_method_id, 'método de pago')
    get_data(db, PaymentWay, request.payment_way_id, 'forma de pago')

    if request.status_id is not None:
        get_data(db, Status, request.status_id, 'estatus')
        request_dict = request.dict()
    else:
        request_dict = request.dict()
        request_dict.pop('status_id')

    return update_data(db, MIPPaymentForm, model_id, model_name, request_dict)


def delete(db: Session, model_id: UUID4):
    return update_delete(db, MIPPaymentForm, model_id, model_name)
