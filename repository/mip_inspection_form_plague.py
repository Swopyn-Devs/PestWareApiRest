from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.mip_inspection_form import MIPInspectionForm
from models.plague import Plague
from models.infestation_degree import InfestationDegree
from models.nesting_area import NestingArea
from models.mip_inspection_form_plague import MIPInspectionFormPlague
from schemas.mip_inspection_form_plague import MIPInspectionFormPlagueRequest

model_name = 'formulario de inspección de plaga MIP'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool, mip_inspection_form_id: UUID4):
    return get_all_data(db, MIPInspectionFormPlague, authorize, paginate_param, False, {'mip_inspection_form_id': mip_inspection_form_id})


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, MIPInspectionFormPlague, model_id, model_name)


def create(db: Session, request: MIPInspectionFormPlagueRequest, model_id: UUID4):
    get_data(db, MIPInspectionForm, model_id, 'formulario de inspección MIP')
    get_data(db, Plague, request.plague_id, 'plaga')
    get_data(db, InfestationDegree, request.infestation_degree_id, 'grado de infestación')

    nesting_area_id = None
    if request.nesting_area_id is not None:
        get_data(db, NestingArea, request.nesting_area_id, 'aŕea de anidación')
        nesting_area_id = request.nesting_area_id

    request_data = MIPInspectionFormPlague(
        mip_inspection_form_id=model_id,
        plague_id=request.plague_id,
        infestation_degree_id=request.infestation_degree_id,
        nesting_area_id=nesting_area_id,
        comments=request.comments
    )
    last_id = insert_data(db, request_data)
    return get_data(db, MIPInspectionFormPlague, last_id, model_name)


def update(db: Session, request: MIPInspectionFormPlagueRequest, model_id: UUID4):
    get_data(db, Plague, request.plague_id, 'plaga')
    get_data(db, InfestationDegree, request.infestation_degree_id, 'grado de infestación')

    if request.nesting_area_id is not None:
        get_data(db, NestingArea, request.nesting_area_id, 'aŕea de anidación')

    return update_data(db, MIPInspectionFormPlague, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, MIPInspectionFormPlague, model_id, model_name)
