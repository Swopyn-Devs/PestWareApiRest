from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.quote_extra import QuoteExtra
from models.quote import Quote
from models.extra import Extra
from schemas.quote_extra import QuoteExtraRequest

model_name = 'extra de la cotización'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool, quote_id: UUID4):
    return get_all_data(db, QuoteExtra, authorize, paginate_param, False, {'quote_id': quote_id})


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, QuoteExtra, model_id, model_name)


def create(db: Session, request: QuoteExtraRequest, model_id: UUID4):
    get_data(db, Quote, model_id, 'cotización')
    get_data(db, Extra, request.extra_id, 'extra')
    request_data = QuoteExtra(
        quote_id=model_id,
        extra_id=request.extra_id,
        quantity=request.quantity
    )
    last_id = insert_data(db, request_data)
    return get_data(db, QuoteExtra, last_id, model_name)


def update(db: Session, request: QuoteExtraRequest, model_id: UUID4):
    get_data(db, Plague, request.extra_id, 'extra')
    return update_data(db, QuoteExtra, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, QuoteExtra, model_id, model_name)
