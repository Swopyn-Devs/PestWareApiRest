from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.quote_plague import QuotePlague
from models.quote import Quote
from models.plague import Plague
from schemas.quote_plague import QuotePlagueRequest

model_name = 'plaga de la cotización'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool, quote_id: UUID4):
    return get_all_data(db, QuotePlague, authorize, paginate_param, False, {'quote_id': quote_id})


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, QuotePlague, model_id, model_name)


def create(db: Session, request: QuotePlagueRequest, model_id: UUID4):
    get_data(db, Quote, model_id, 'cotización')
    get_data(db, Plague, request.plague_id, 'plaga')
    request_data = QuotePlague(
        quote_id=model_id,
        plague_id=request.plague_id
    )
    last_id = insert_data(db, request_data)
    return get_data(db, QuotePlague, last_id, model_name)


def update(db: Session, request: QuotePlagueRequest, model_id: UUID4):
    get_data(db, Plague, request.plague_id, 'plaga')
    return update_data(db, QuotePlague, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, QuotePlague, model_id, model_name)
