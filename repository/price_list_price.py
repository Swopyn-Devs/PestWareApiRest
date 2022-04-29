from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.price_list_prices import PriceListPrice
from schemas.price_list_price import PriceListPriceRequest, PriceListPriceUpdateRequest

model_name = 'precio(s) de lista de precio'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool, price_list_id: UUID4):
    return get_all_data(db, PriceListPrice, authorize, paginate_param, False, {'price_list_id': price_list_id})


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, PriceListPrice, model_id, model_name, False)


def create(db: Session, request: PriceListPriceRequest, model_id: UUID4):
    request_data = PriceListPrice(
        price_list_id=model_id,
        scale=request.scale,
        price_one=request.price_one,
        price_two=request.price_two
    )
    insert_data(db, request_data)
    return request_data


def update(db: Session, request: PriceListPriceUpdateRequest, model_id: UUID4):
    return update_data(db, PriceListPrice, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, PriceListPrice, model_id, model_name)
