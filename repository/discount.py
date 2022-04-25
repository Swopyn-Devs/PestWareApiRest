from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.discount import Discount
from schemas.discount import DiscountRequest, DiscountUpdateRequest

model_name = 'descuento'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, Discount, authorize, paginate_param, True)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, Discount, model_id, model_name)


def create(db: Session, request: DiscountRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = Discount(
        name=request.name,
        description=request.description,
        percentage=request.percentage,
        job_center_id=employee.job_center_id
    )
    insert_data(db, request_data)
    return request_data


def update(db: Session, request: DiscountUpdateRequest, model_id: UUID4):
    return update_data(db, Discount, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, Discount, model_id, model_name)
