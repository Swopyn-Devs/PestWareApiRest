from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session

from models.payment_method import PaymentMethod
from schemas.payment_method import PaymentMethodRequest

model_name = 'método de pago'


def get_all(db: Session):
    return get_all_data(db, PaymentMethod)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, PaymentMethod, model_id, model_name)


def create(db: Session, request: PaymentMethodRequest):
    request_data = PaymentMethod(
        name=request.name,
        job_center_id=request.job_center_id,
    )
    insert_data(db, request_data)
    return request_data


def update(db: Session, request: PaymentMethodRequest, model_id: UUID4):
    return update_data(db, PaymentMethod, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, PaymentMethod, model_id, model_name)
