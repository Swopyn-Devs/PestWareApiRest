from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.quote import Quote
from models.quote_tracing import QuoteTracing
from schemas.quote_tracing import QuoteTracingRequest

model_name = 'seguimiento de la cotización'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool, quote_id: UUID4):
    return get_all_data(db, QuoteTracing, authorize, paginate_param, False, {'quote_id': quote_id})


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, QuoteTracing, model_id, model_name)


def create(db: Session, request: QuoteTracingRequest, model_id: UUID4):
    get_data(db, Quote, model_id, 'cotización')
    request_data = QuoteTracing(
        quote_id=model_id,
        date=request.date,
        time=request.time,
        comment=request.comment
    )
    last_id = insert_data(db, request_data)
    return get_data(db, QuoteTracing, last_id, model_name)


def update(db: Session, request: QuoteTracingRequest, model_id: UUID4):
    return update_data(db, QuoteTracing, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, QuoteTracing, model_id, model_name)
