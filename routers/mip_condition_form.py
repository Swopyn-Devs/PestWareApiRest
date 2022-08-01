from fastapi import APIRouter, Depends, status, Query, UploadFile
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional, List

from database import get_db
from repository import mip_condition_form
from repository import mip_condition_form_cleaning
from repository import mip_condition_form_photo
from schemas.mip_condition_form import MIPConditionFormRequest, MIPConditionFormResponse
from schemas.mip_condition_form_cleaning import MIPConditionFormCleaningRequest, MIPConditionFormCleaningResponse
from schemas.mip_condition_form_photo import MIPConditionFormPhotoRequest, MIPConditionFormPhotoResponse

router = APIRouter(
    prefix='/mip-condition-form',
    tags=['🧰 Formulario de condición MIP']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[MIPConditionFormResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_condition_form.get_all(db, authorize, paginate)


@router.get('/{mip_condition_form_id}/cleaning', status_code=status.HTTP_200_OK, response_model=Page[MIPConditionFormCleaningResponse])
async def index_cleaning(mip_condition_form_id: UUID4, paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_condition_form_cleaning.get_all(db, authorize, paginate, mip_condition_form_id)


@router.get('/{mip_condition_form_id}/photos', status_code=status.HTTP_200_OK, response_model=Page[MIPConditionFormPhotoResponse])
async def index_photo(mip_condition_form_id: UUID4, paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_condition_form_photo.get_all(db, authorize, paginate, mip_condition_form_id)


@router.get('/{mip_condition_form_id}', status_code=status.HTTP_200_OK, response_model=MIPConditionFormResponse)
async def show(mip_condition_form_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_condition_form.retrieve(db, mip_condition_form_id)


@router.get('/cleaning/{mip_condition_form_cleaning_id}', status_code=status.HTTP_200_OK, response_model=MIPConditionFormCleaningResponse)
async def show_cleaning(mip_condition_form_cleaning_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_condition_form_cleaning.retrieve(db, mip_condition_form_cleaning_id)


@router.get('/photos/{mip_condition_form_photo_id}', status_code=status.HTTP_200_OK, response_model=MIPConditionFormPhotoResponse)
async def show_photo(mip_condition_form_photo_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_condition_form_photo.retrieve(db, mip_condition_form_photo_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=MIPConditionFormResponse)
async def store(request: MIPConditionFormRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_condition_form.create(db, request)


@router.post('/{mip_condition_form_id}/cleaning', status_code=status.HTTP_201_CREATED, response_model=MIPConditionFormCleaningResponse)
async def store_cleaning(mip_condition_form_id: UUID4, request: MIPConditionFormCleaningRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_condition_form_cleaning.create(db, request, mip_condition_form_id)


@router.post('/{mip_condition_form_id}/photos', status_code=status.HTTP_201_CREATED, response_model=Page[MIPConditionFormPhotoResponse])
async def store_photo(mip_condition_form_id: UUID4, request: MIPConditionFormPhotoRequest, files: List[UploadFile], db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_condition_form_photo.create(db, authorize, files, request, mip_condition_form_id)


@router.put('/{mip_condition_form_id}', status_code=status.HTTP_202_ACCEPTED, response_model=MIPConditionFormResponse)
async def update(mip_condition_form_id: UUID4, request: MIPConditionFormRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_condition_form.update(db, request, mip_condition_form_id)


@router.put('/cleaning/{mip_condition_form_cleaning_id}', status_code=status.HTTP_202_ACCEPTED, response_model=MIPConditionFormCleaningResponse)
async def update_cleaning(mip_condition_form_cleaning_id: UUID4, request: MIPConditionFormCleaningRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_condition_form_cleaning.update(db, request, mip_condition_form_cleaning_id)


@router.put('/photos/{mip_condition_form_photo_id}', status_code=status.HTTP_202_ACCEPTED, response_model=MIPConditionFormPhotoResponse)
async def update_photo(mip_condition_form_photo_id: UUID4, request: MIPConditionFormPhotoRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_condition_form_photo.update(db, request, mip_condition_form_photo_id)


@router.delete('/{mip_condition_form_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(mip_condition_form_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_condition_form.delete(db, mip_condition_form_id)


@router.delete('/cleaning/{mip_condition_form_cleaning_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy_cleaning(mip_condition_form_cleaning_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_condition_form_cleaning.delete(db, mip_condition_form_cleaning_id)


@router.delete('/photos/{mip_condition_form_photo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy_photos(mip_condition_form_photo_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_condition_form_photo.delete(db, mip_condition_form_photo_id)
