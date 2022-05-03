from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.price_list_plague import PriceListPlague
from models.price_list import PriceList
from models.plague import Plague
from schemas.price_list_plague import PriceListPlagueRequest

model_name = 'plaga de lista de precio'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool, price_list_id: UUID4):
    return get_all_data(db, PriceListPlague, authorize, paginate_param, False, {'price_list_id': price_list_id})


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, PriceListPlague, model_id, model_name)


def create(db: Session, request: PriceListPlagueRequest, model_id: UUID4):
    get_data(db, PriceList, model_id, 'lista de precio')
    get_data(db, Plague, request.plague_id, 'plaga')
    request_data = PriceListPlague(
        price_list_id=model_id,
        plague_id=request.plague_id
    )
    insert_data(db, request_data)
    return request_data


def update(db: Session, request: PriceListPlagueRequest, model_id: UUID4):
    get_data(db, Plague, request.plague_id, 'plaga')
    return update_data(db, PriceListPlague, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, PriceListPlague, model_id, model_name)
