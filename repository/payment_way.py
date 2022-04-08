from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session

from models.payment_way import PaymentWay
from schemas.payment_way import PaymentWayRequest

model_name = 'forma de pago'


def get_all(db: Session):
    return get_all_data(db, PaymentWay)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, PaymentWay, model_id, model_name)


def create(db: Session, request: PaymentWayRequest):
    request_data = PaymentWay(
        name=request.name,
        credit_days=request.credit_days,
        job_center_id=request.job_center_id,
    )
    insert_data(db, request_data)
    return request_data


def update(db: Session, request: PaymentWayRequest, model_id: UUID4):
    return update_data(db, PaymentWay, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, PaymentWay, model_id, model_name)
