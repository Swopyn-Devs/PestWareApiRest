from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from decouple import config
from fastapi import UploadFile
from fastapi_jwt_auth import AuthJWT
from services import aws
from typing import List

from models.mip_condition_form import MIPConditionForm
from models.mip_condition_form_photo import MIPConditionFormPhoto
from schemas.mip_condition_form_photo import MIPConditionFormPhotoRequest

model_name = 'formulario de condición de foto MIP'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool, mip_condition_form_id: UUID4):
    return get_all_data(db, MIPConditionFormPhoto, authorize, paginate_param, False, {'mip_condition_form_id': mip_condition_form_id})


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, MIPConditionFormPhoto, model_id, model_name)


def create(db: Session, authorize: AuthJWT, photos: List[UploadFile], request: MIPConditionFormPhotoRequest, model_id: UUID4):
    get_data(db, MIPConditionForm, model_id, 'formulario de condición MIP')
    for photo in photos:
        validate_image(photo)
        request_data = MIPConditionFormPhoto(
            mip_condition_form_id=model_id,
            comments=request.comments,
            photo=""
        )
        last_id = insert_data(db, request_data)
        key = f'conditions/{model_id}/photos/{last_id}.jpeg'

        if not aws.upload_image(config('AWS_S3_BUCKET_MIP_FORM'), key, photo):
            delete_record(db, MIPConditionFormPhoto, last_id)

        update_data(db, MIPConditionFormPhoto, last_id, model_name, {'photo': key})
    return get_all_data(db, MIPConditionFormPhoto, authorize, False, False, {'mip_condition_form_id': model_id})


def update(db: Session, request: MIPConditionFormPhotoRequest, model_id: UUID4):
    return update_data(db, MIPConditionFormPhoto, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    data = get_data(db, MIPConditionFormPhoto, model_id, model_name)
    mip_condition_form_id = data['mip_condition_form_id']['id']
    key = f'conditions/{mip_condition_form_id}/photos/{model_id}.jpeg'

    if not aws.delete_file(config('AWS_S3_BUCKET_MIP_FORM'), key):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=file_error_deleted('foto'))

    return update_delete(db, MIPConditionFormPhoto, model_id, model_name)
