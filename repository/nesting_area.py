from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.customer import Customer
from models.nesting_area import NestingArea
from schemas.nesting_area import NestingAreaRequest

model_name = 'área de anidación'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, NestingArea, authorize, paginate_param, False)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, NestingArea, model_id, model_name)


def create(db: Session, request: NestingAreaRequest):
    get_data(db, Customer, request.customer_id, 'cliente')
    request_data = NestingArea(
        name=request.name,
        customer_id=request.customer_id
    )
    last_id = insert_data(db, request_data)
    return get_data(db, NestingArea, last_id, model_name)


def update(db: Session, request: NestingAreaRequest, model_id: UUID4):
    get_data(db, Customer, request.customer_id, 'cliente')
    return update_data(db, NestingArea, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, NestingArea, model_id, model_name)
