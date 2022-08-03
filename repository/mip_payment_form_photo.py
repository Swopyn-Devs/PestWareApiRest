from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from decouple import config
from fastapi import UploadFile
from fastapi_jwt_auth import AuthJWT
from services import aws
from typing import List

from models.mip_payment_form import MIPPaymentForm
from models.mip_payment_form_photo import MIPPaymentFormPhoto
from schemas.mip_payment_form_photo import MIPPaymentFormPhotoRequest
model_name = 'formulario de pago de foto MIP'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool, mip_payment_form_id: UUID4):
    return get_all_data(db, MIPPaymentFormPhoto, authorize, paginate_param, False, {'mip_payment_form_id': mip_payment_form_id})


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, MIPPaymentFormPhoto, model_id, model_name)


def create(db: Session, authorize: AuthJWT, photos: List[UploadFile], request: MIPPaymentFormPhotoRequest, model_id: UUID4):
    get_data(db, MIPPaymentForm, model_id, 'formulario de pago MIP')
    for photo in photos:
        validate_image(photo)
        request_data = MIPPaymentFormPhoto(
            mip_payment_form_id=model_id,
            comments=request.comments,
            photo=""
        )
        last_id = insert_data(db, request_data)
        key = f'payment/{model_id}/photos/{last_id}.jpeg'

        if not aws.upload_image(config('AWS_S3_BUCKET_MIP_FORM'), key, photo):
            delete_record(db, MIPPaymentFormPhoto, last_id)

        update_data(db, MIPPaymentFormPhoto, last_id, model_name, {'photo': key})
    return get_all_data(db, MIPPaymentFormPhoto, authorize, False, False, {'mip_payment_form_id': model_id})


def update(db: Session, request: MIPPaymentFormPhotoRequest, model_id: UUID4):
    return update_data(db, MIPPaymentFormPhoto, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    data = get_data(db, MIPPaymentFormPhoto, model_id, model_name)
    mip_payment_form_id = data['mip_payment_form_id']['id']
    key = f'payment/{mip_payment_form_id}/photos/{model_id}.jpeg'

    if not aws.delete_file(config('AWS_S3_BUCKET_MIP_FORM'), key):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=file_error_deleted('foto'))

    return update_delete(db, MIPPaymentFormPhoto, model_id, model_name)
