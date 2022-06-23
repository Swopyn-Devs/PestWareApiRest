from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.concept import Concept
from schemas.concept import ConceptRequest, ConceptUpdateRequest

model_name = 'concepto'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, Concept, authorize, paginate_param, True)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, Concept, model_id, model_name)


def create(db: Session, request: ConceptRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = Concept(
        name=request.name,
        type=request.type,
        job_center_id=employee.job_center_id,
    )
    last_id = insert_data(db, request_data)
    return get_data(db, Concept, last_id, model_name)


def update(db: Session, request: ConceptUpdateRequest, model_id: UUID4):
    return update_data(db, Concept, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, Concept, model_id, model_name)
