from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.payment_method import PaymentMethod
from schemas.payment_method import PaymentMethodRequest, PaymentMethodUpdateRequest

model_name = 'método de pago'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, PaymentMethod, authorize, paginate_param, True)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, PaymentMethod, model_id, model_name)


def create(db: Session, request: PaymentMethodRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = PaymentMethod(
        name=request.name,
        job_center_id=employee.job_center_id,
    )
    insert_data(db, request_data)
    return request_data


def update(db: Session, request: PaymentMethodUpdateRequest, model_id: UUID4):
    return update_data(db, PaymentMethod, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, PaymentMethod, model_id, model_name)
