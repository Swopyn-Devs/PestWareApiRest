from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.plague_category import PlagueCategory
from schemas.plague_category import PlagueCategoryRequest, PlagueCategoryUpdateRequest

model_name = 'categoría de plaga'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, PlagueCategory, authorize, paginate_param, True)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, PlagueCategory, model_id, model_name)


def create(db: Session, request: PlagueCategoryRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = PlagueCategory(
        name=request.name,
        job_center_id=employee.job_center_id,
    )
    insert_data(db, request_data)
    return request_data


def update(db: Session, request: PlagueCategoryUpdateRequest, model_id: UUID4):
    return update_data(db, PlagueCategory, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, PlagueCategory, model_id, model_name)
