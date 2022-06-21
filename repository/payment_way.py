from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.payment_way import PaymentWay
from schemas.payment_way import PaymentWayRequest, PaymentWayUpdateRequest

model_name = 'forma de pago'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, PaymentWay, authorize, paginate_param, True)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, PaymentWay, model_id, model_name)


def create(db: Session, request: PaymentWayRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = PaymentWay(
        name=request.name,
        credit_days=request.credit_days,
        job_center_id=employee.job_center_id,
    )
    last_id = insert_data(db, request_data)
    return get_data(db, PaymentWay, last_id, model_name)


def update(db: Session, request: PaymentWayUpdateRequest, model_id: UUID4):
    return update_data(db, PaymentWay, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, PaymentWay, model_id, model_name)
