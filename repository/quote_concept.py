from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.quote_concept import QuoteConcept
from models.quote import Quote
from schemas.quote_concept import QuoteConceptRequest

model_name = 'concepto de la cotización'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool, quote_id: UUID4):
    return get_all_data(db, QuoteConcept, authorize, paginate_param, False, {'quote_id': quote_id})


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, QuoteConcept, model_id, model_name)


def create(db: Session, request: QuoteConceptRequest, model_id: UUID4):
    get_data(db, Quote, model_id, 'cotización')
    request_data = QuoteConcept(
        quote_id=model_id,
        concept=request.concept,
        quantity=request.quantity,
        unit_price=request.unit_price,
        tax=request.tax,
        subtotal=request.subtotal,
        total=request.total
    )
    last_id = insert_data(db, request_data)
    return get_data(db, QuoteConcept, last_id, model_name)


def update(db: Session, request: QuoteConceptRequest, model_id: UUID4):
    return update_data(db, QuoteConcept, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, QuoteConcept, model_id, model_name)
