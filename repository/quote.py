from utils.functions import *
from utils import folios

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.quote import Quote
from models.service_type import ServiceType
from models.customer import Customer
from models.origin_source import OriginSource
from models.employee import Employee
from models.status import Status
from models.job_center import JobCenter
from schemas.quote import QuoteRequest, QuoteUpdateRequest

model_name = 'cotización'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, Quote, authorize, paginate_param, True)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, Quote, model_id, model_name)


def create(db: Session, request: QuoteRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    get_data(db, ServiceType, request.service_type_id, 'tipo de servicio')
    get_data(db, Customer, request.customer_id, 'cliente')
    get_data(db, OriginSource, request.origin_source_id, 'fuente de origen')
    get_data(db, Employee, request.employee_id, 'empleado')
    folio = folios.quote(db, employee.job_center_id)
    request_data = Quote(
        folio=folio,
        total=request.total,
        description=request.description,
        service_type_id=request.service_type_id,
        customer_id=request.customer_id,
        origin_source_id=request.origin_source_id,
        employee_id=request.employee_id,
        status_id=get_status_id(),
        job_center_id=employee.job_center_id
    )
    last_id = insert_data(db, request_data)
    return get_data(db, Quote, last_id, model_name)


def update(db: Session, request: QuoteUpdateRequest, model_id: UUID4):
    get_data(db, ServiceType, request.service_type_id, 'tipo de servicio')
    get_data(db, Customer, request.customer_id, 'cliente')
    get_data(db, OriginSource, request.origin_source_id, 'fuente de origen')
    get_data(db, Employee, request.employee_id, 'empleado')
    get_data(db, JobCenter, request.job_center_id, 'centro de trabajo')
    return update_data(db, Quote, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, Quote, model_id, model_name)
