from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.rejection_reason import RejectionReason
from schemas.rejection_reason import RejectionReasonRequest, RejectionReasonUpdateRequest

model_name = 'motivo de rechazo'


def get_all(db: Session, authorize: AuthJWT):
    return get_all_data(db, RejectionReason, authorize)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, RejectionReason, model_id, model_name)


def create(db: Session, request: RejectionReasonRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = RejectionReason(
        name=request.name,
        job_center_id=employee.job_center_id
    )
    insert_data(db, request_data)
    return request_data


def update(db: Session, request: RejectionReasonUpdateRequest, model_id: UUID4):
    return update_data(db, RejectionReason, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, RejectionReason, model_id, model_name)
