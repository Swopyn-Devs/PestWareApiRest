from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session

from models.voucher import Voucher
from schemas.voucher import VoucherRequest

model_name = 'comprobante'


def get_all(db: Session):
    return get_all_data(db, Voucher)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, Voucher, model_id, model_name)


def create(db: Session, request: VoucherRequest):
    request_data = Voucher(
        name=request.name,
        job_center_id=request.job_center_id,
    )
    insert_data(db, request_data)
    return request_data


def update(db: Session, request: VoucherRequest, model_id: UUID4):
    return update_data(db, Voucher, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, Voucher, model_id, model_name)
