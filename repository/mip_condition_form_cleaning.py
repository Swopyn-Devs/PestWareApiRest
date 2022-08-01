from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.mip_condition_form import MIPConditionForm
from models.cleaning import Cleaning
from models.mip_condition_form_cleaning import MIPConditionFormCleaning
from schemas.mip_condition_form_cleaning import MIPConditionFormCleaningRequest

model_name = 'formulario de condición de orden y limpieza MIP'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool, mip_condition_form_id: UUID4):
    return get_all_data(db, MIPConditionFormCleaning, authorize, paginate_param, False, {'mip_condition_form_id': mip_condition_form_id})


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, MIPConditionFormCleaning, model_id, model_name)


def create(db: Session, request: MIPConditionFormCleaningRequest, model_id: UUID4):
    get_data(db, MIPConditionForm, model_id, 'formulario de condición MIP')
    get_data(db, Cleaning, request.cleaning_id, 'orden y limpieza')

    request_data = MIPConditionFormCleaning(
        mip_condition_form_id=model_id,
        cleaning_id=request.cleaning_id
    )
    last_id = insert_data(db, request_data)
    return get_data(db, MIPConditionFormCleaning, last_id, model_name)


def update(db: Session, request: MIPConditionFormCleaningRequest, model_id: UUID4):
    get_data(db, Cleaning, request.cleaning_id, 'orden y limpieza')
    return update_data(db, MIPConditionFormCleaning, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, MIPConditionFormCleaning, model_id, model_name)
