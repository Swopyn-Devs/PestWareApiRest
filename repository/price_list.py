from utils.functions import *
from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
from models.price_list import PriceList
from models.service_type import ServiceType
from schemas.price_list import PriceListRequest

model_name = 'lista de precio'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, PriceList, authorize, paginate_param, True)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, PriceList, model_id, model_name)


def create(db: Session, request: PriceListRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    get_data(db, ServiceType, request.service_type_id, 'tipo de servicio')
    request_data = PriceList(
        name=request.name,
        key=request.key,
        hierarchy=request.hierarchy,
        cost=request.cost,
        min_cost=request.min_cost,
        service_type_id=request.service_type_id,
        job_center_id=employee.job_center_id
    )
    last_id = insert_data(db, request_data)
    return get_data(db, PriceList, last_id, model_name)


def update(db: Session, request: PriceListRequest, model_id: UUID4):
    get_data(db, ServiceType, request.service_type_id, 'tipo de servicio')
    return update_data(db, PriceList, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, PriceList, model_id, model_name)
