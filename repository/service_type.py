from utils.functions import *
from decouple import config
from fastapi import UploadFile
from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
from services import aws
from models.service_type import ServiceType
from models.indication import Indication
from schemas.service_type import ServiceTypeRequest, ServiceTypeUpdateRequest

model_name = 'tipo de servicio'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    data = db.query(ServiceType).filter(ServiceType.is_deleted == False).all()

    for item in data:
        if item.cover is not None:
            item.cover = map_s3_url(config('AWS_S3_URL_SERVICE_TYPES'), item.cover)

    # set data model to foreign field
    aux = 0
    data_main = data
    for record in data_main:
        data2 = object_as_dict(record)
        for field in data2:
            model2 = get_model(field)
            if model2 != False:
                data_model = get_data(db, model2[0], data2[field], model2[1], False, False, False)
                if field == 'customer_id':
                        data_model = customer.response_customer(db, data_model)
                data_main[aux] = update_field(data_main[aux], field, data_model)
        aux += 1
    data = data_main

    if paginate_param == True:
        return paginate(data)
    elif paginate_param == 'all':
        return data

    data_size = len(data)
    if data_size <= 0:
        data_size = 1
    return paginate(data, Params(size=data_size))


def retrieve(db: Session, model_id: UUID4):
    data = get_data(db, ServiceType, model_id, model_name)
    if data.cover is not None:
        data.cover = map_s3_url(config('AWS_S3_URL_SERVICE_TYPES'), data.cover)
    return data


def create(db: Session, request: ServiceTypeRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    get_data(db, Indication, request.indication_id, 'indicación')
    request_data = ServiceType(
        name=request.name,
        frequency_days=request.frequency_days,
        certificate_expiration_days=request.certificate_expiration_days,
        follow_up_days=request.follow_up_days,
        disinfection=request.disinfection,
        show_price=request.show_price,
        indication_id=request.indication_id,
        job_center_id=employee.job_center_id
    )
    last_id = insert_data(db, request_data)
    return get_data(db, ServiceType, last_id, model_name)


def update(db: Session, request: ServiceTypeUpdateRequest, model_id: UUID4):
    get_data(db, Indication, request.indication_id, 'indicación')
    return update_data(db, ServiceType, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, ServiceType, model_id, model_name)


def update_cover(db: Session, file: UploadFile, model_id):
    validate_pdf(file)
    key = f'covers/{model_id}.pdf'
    response_update_data = update_data(db, ServiceType, model_id, model_name, {'cover': key})

    if not aws.upload_image(config('AWS_S3_BUCKET_SERVICE_TYPES'), key, file):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=file_error_updated('PDF'))

    if response_update_data.cover is not None:
        response_update_data.cover = map_s3_url(config('AWS_S3_URL_SERVICE_TYPES'), response_update_data.cover)
    return response_update_data


def delete_cover(db: Session, model_id: UUID4):
    key = f'covers/{model_id}.pdf'
    response_update_data = update_data(db, ServiceType, model_id, model_name, {'cover': None})

    if not aws.delete_file(config('AWS_S3_BUCKET_SERVICE_TYPES'), key):
        update_data(db, ServiceType, model_id, model_name, {'cover': key})
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=file_error_deleted('PDF'))

    if response_update_data.cover is not None:
        response_update_data.cover = map_s3_url(config('AWS_S3_URL_SERVICE_TYPES'), response_update_data.cover)
    return response_update_data
