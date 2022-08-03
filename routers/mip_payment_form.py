from fastapi import APIRouter, Depends, status, Query, UploadFile
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional, List

from database import get_db
from repository import mip_payment_form
from repository import mip_payment_form_photo
from schemas.mip_payment_form import MIPPaymentFormRequest, MIPPaymentFormResponse
from schemas.mip_payment_form_photo import MIPPaymentFormPhotoRequest, MIPPaymentFormPhotoResponse

router = APIRouter(
    prefix='/mip-payment-form',
    tags=['🪙 Formulario de pago MIP']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[MIPPaymentFormResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_payment_form.get_all(db, authorize, paginate)


@router.get('/{mip_payment_form_id}/photos', status_code=status.HTTP_200_OK, response_model=Page[MIPPaymentFormPhotoResponse])
async def index_photo(mip_payment_form_id: UUID4, paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_payment_form_photo.get_all(db, authorize, paginate, mip_payment_form_id)


@router.get('/{mip_payment_form_id}', status_code=status.HTTP_200_OK, response_model=MIPPaymentFormResponse)
async def show(mip_payment_form_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_payment_form.retrieve(db, mip_payment_form_id)


@router.get('/photos/{mip_payment_form_photo_id}', status_code=status.HTTP_200_OK, response_model=MIPPaymentFormPhotoResponse)
async def show_photo(mip_payment_form_photo_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_payment_form_photo.retrieve(db, mip_payment_form_photo_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=MIPPaymentFormResponse)
async def store(request: MIPPaymentFormRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_payment_form.create(db, request)


@router.post('/{mip_payment_form_id}/photos', status_code=status.HTTP_201_CREATED, response_model=Page[MIPPaymentFormPhotoResponse])
async def store_photo(mip_payment_form_id: UUID4, request: MIPPaymentFormPhotoRequest, files: List[UploadFile], db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_payment_form_photo.create(db, authorize, files, request, mip_payment_form_id)


@router.put('/{mip_payment_form_id}', status_code=status.HTTP_202_ACCEPTED, response_model=MIPPaymentFormResponse)
async def update(mip_payment_form_id: UUID4, request: MIPPaymentFormRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_payment_form.update(db, request, mip_payment_form_id)


@router.put('/photos/{mip_payment_form_photo_id}', status_code=status.HTTP_202_ACCEPTED, response_model=MIPPaymentFormPhotoResponse)
async def update_photo(mip_payment_form_photo_id: UUID4, request: MIPPaymentFormPhotoRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_payment_form_photo.update(db, request, mip_payment_form_photo_id)


@router.delete('/{mip_payment_form_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(mip_payment_form_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_payment_form.delete(db, mip_payment_form_id)


@router.delete('/photos/{mip_payment_form_photo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy_photos(mip_payment_form_photo_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_payment_form_photo.delete(db, mip_payment_form_photo_id)
