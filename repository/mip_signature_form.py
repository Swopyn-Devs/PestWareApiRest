from utils.functions import *

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
from fastapi import UploadFile
from decouple import config
from services import aws

from models.event_type import EventType
from models.mip_signature_form import MIPSignatureForm
from schemas.mip_signature_form import MIPSignatureFormRequest

model_name = 'formulario de firma MIP'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, MIPSignatureForm, authorize, paginate_param)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, MIPSignatureForm, model_id, model_name)


def create(db: Session, request: MIPSignatureFormRequest):
    get_data(db, EventType, request.event_id, 'tipo de evento')
    request_data = MIPSignatureForm(
        event_id=request.event_id,
        signature='',
        name=request.name
    )
    last_id = insert_data(db, request_data)
    return get_data(db, MIPSignatureForm, last_id, model_name)


def update_signature(db: Session, photo: UploadFile, model_id: UUID4):
    validate_image(photo)
    key = f'signatures/{model_id}/photos/signature.jpeg'

    if not aws.upload_image(config('AWS_S3_BUCKET_MIP_FORM'), key, photo):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=file_error_updated('firma'))

    return update_data(db, MIPSignatureForm, model_id, model_name, {'signature': key})


def update(db: Session, request: MIPSignatureFormRequest, model_id: UUID4):
    get_data(db, EventType, request.event_id, 'tipo de evento')
    return update_data(db, MIPSignatureForm, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    key = f'signatures/{model_id}/photos/signature.jpeg'

    if not aws.delete_file(config('AWS_S3_BUCKET_MIP_FORM'), key):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=file_error_deleted('foto'))

    return update_delete(db, MIPSignatureForm, model_id, model_name)
