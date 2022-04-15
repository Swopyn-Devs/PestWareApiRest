from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.infestation_degree import InfestationDegree
from schemas.infestation_degree import InfestationDegreeRequest, InfestationDegreeUpdateRequest

model_name = 'grado de infestación'


def get_all(db: Session, authorize: AuthJWT):
    return get_all_data(db, InfestationDegree, authorize)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, InfestationDegree, model_id, model_name)


def create(db: Session, request: InfestationDegreeRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = InfestationDegree(
        name=request.name,
        job_center_id=employee.job_center_id,
    )
    insert_data(db, request_data)
    return request_data


def update(db: Session, request: InfestationDegreeUpdateRequest, model_id: UUID4):
    return update_data(db, InfestationDegree, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, InfestationDegree, model_id, model_name)
