from utils.functions import *
from decouple import config
from fastapi import UploadFile
from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
from services import aws
from models.price_list import PriceList
from models.service_type import ServiceType
from models.indication import Indication
from schemas.price_list import PriceListRequest

model_name = 'lista de precio'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, PriceList, authorize, paginate_param, True)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, PriceList, model_id, model_name)


def create(db: Session, request: PriceListRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    get_data(db, ServiceType, request.service_type_id, 'tipo de servicio')
    get_data(db, Indication, request.indication_id, 'indicación')
    request_data = PriceList(
        name=request.name,
        key=request.key,
        hierarchy=request.hierarchy,
        cost=request.cost,
        frequency_days=request.frequency_days,
        certificate_expiration_days=request.certificate_expiration_days,
        show_price=request.show_price,
        disinfection=request.disinfection,
        service_type_id=request.service_type_id,
        indication_id=request.indication_id,
        job_center_id=employee.job_center_id
    )
    insert_data(db, request_data)
    return request_data


def update(db: Session, request: PriceListRequest, model_id: UUID4):
    get_data(db, ServiceType, request.service_type_id, 'tipo de servicio')
    get_data(db, Indication, request.indication_id, 'indicación')
    return update_data(db, PriceList, model_id, model_name, request.dict())


def update_cover(db: Session, file: UploadFile, model_id, authorize: AuthJWT):
    validate_pdf(file)
    key = f'covers/{model_id}.pdf'
    response_update_data = update_data(db, PriceList, model_id, model_name, {'cover': key})

    if not aws.upload_image(config('AWS_S3_BUCKET_PRICE_LISTS'), key, file):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f'No fue posible actualizar el archivo PDF.')

    if response_update_data.cover is not None:
        response_update_data.cover = map_s3_url(config('AWS_S3_URL_PRICE_LISTS'), response_update_data.cover)
    return response_update_data


def delete_cover(db: Session, model_id: UUID4):
    key = f'covers/{model_id}.pdf'
    response_update_data = update_data(db, PriceList, model_id, model_name, {'cover': None})

    if not aws.delete_file(config('AWS_S3_BUCKET_PRICE_LISTS'), key):
        update_data(db, PriceList, model_id, model_name, {'cover': key})
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f'No fue posible eliminar el archivo PDF.')

    if response_update_data.cover is not None:
        response_update_data.cover = map_s3_url(config('AWS_S3_URL_PRICE_LISTS'), response_update_data.cover)
    return response_update_data


def delete(db: Session, model_id: UUID4):
    return update_delete(db, PriceList, model_id, model_name)
