from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT

from models.supplier import Supplier
from schemas.supplier import SupplierRequest, SupplierUpdateRequest

model_name = 'proveedor'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, Supplier, authorize, paginate_param, True)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, Supplier, model_id, model_name)


def create(db: Session, request: SupplierRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    request_data = Supplier(
        name=request.name,
        contact_name=request.contact_name,
        address=request.address,
        phone=request.phone,
        email=request.email,
        bank=request.bank,
        account_holder=request.account_holder,
        account_number=request.account_number,
        taxpayer_registration=request.taxpayer_registration,
        job_center_id=employee.job_center_id
    )
    last_id = insert_data(db, request_data)
    return get_data(db, Supplier, last_id, model_name)


def update(db: Session, request: SupplierUpdateRequest, model_id: UUID4):
    return update_data(db, Supplier, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, Supplier, model_id, model_name)
