from fastapi import APIRouter, Depends, status, Query, UploadFile
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional, List

from database import get_db
from repository import mip_inspection_form
from repository import mip_inspection_form_plague
from repository import mip_inspection_form_photo
from schemas.mip_inspection_form import MIPInspectionFormRequest, MIPInspectionFormResponse
from schemas.mip_inspection_form_plague import MIPInspectionFormPlagueRequest, MIPInspectionFormPlagueResponse
from schemas.mip_inspection_form_photo import MIPInspectionFormPhotoRequest, MIPInspectionFormPhotoResponse

router = APIRouter(
    prefix='/mip-inspection-form',
    tags=['🗄 Formulario de inspección MIP']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[MIPInspectionFormResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_inspection_form.get_all(db, authorize, paginate)


@router.get('/{mip_inspection_form_id}/plagues', status_code=status.HTTP_200_OK, response_model=Page[MIPInspectionFormPlagueResponse])
async def index_plague(mip_inspection_form_id: UUID4, paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_inspection_form_plague.get_all(db, authorize, paginate, mip_inspection_form_id)


@router.get('/{mip_inspection_form_id}/photos', status_code=status.HTTP_200_OK, response_model=Page[MIPInspectionFormPhotoResponse])
async def index_photo(mip_inspection_form_id: UUID4, paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_inspection_form_photo.get_all(db, authorize, paginate, mip_inspection_form_id)


@router.get('/{mip_inspection_form_id}', status_code=status.HTTP_200_OK, response_model=MIPInspectionFormResponse)
async def show(mip_inspection_form_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_inspection_form.retrieve(db, mip_inspection_form_id)


@router.get('/plagues/{mip_inspection_form_plague_id}', status_code=status.HTTP_200_OK, response_model=MIPInspectionFormPlagueResponse)
async def show_plague(mip_inspection_form_plague_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_inspection_form_plague.retrieve(db, mip_inspection_form_plague_id)


@router.get('/photos/{mip_inspection_form_photo_id}', status_code=status.HTTP_200_OK, response_model=MIPInspectionFormPhotoResponse)
async def show_photo(mip_inspection_form_photo_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_inspection_form_photo.retrieve(db, mip_inspection_form_photo_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=MIPInspectionFormResponse)
async def store(request: MIPInspectionFormRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_inspection_form.create(db, request)


@router.post('/{mip_inspection_form_id}/plagues', status_code=status.HTTP_201_CREATED, response_model=MIPInspectionFormPlagueResponse)
async def store_plague(mip_inspection_form_id: UUID4, request: MIPInspectionFormPlagueRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_inspection_form_plague.create(db, request, mip_inspection_form_id)


@router.post('/{mip_inspection_form_id}/photos', status_code=status.HTTP_201_CREATED, response_model=Page[MIPInspectionFormPhotoResponse])
async def store_photo(mip_inspection_form_id: UUID4, request: MIPInspectionFormPhotoRequest, files: List[UploadFile], db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_inspection_form_photo.create(db, authorize, files, request, mip_inspection_form_id)


@router.put('/{mip_inspection_form_id}', status_code=status.HTTP_202_ACCEPTED, response_model=MIPInspectionFormResponse)
async def update(mip_inspection_form_id: UUID4, request: MIPInspectionFormRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_inspection_form.update(db, request, mip_inspection_form_id)


@router.put('/plagues/{mip_inspection_form_plague_id}', status_code=status.HTTP_202_ACCEPTED, response_model=MIPInspectionFormPlagueResponse)
async def update_plague(mip_inspection_form_plague_id: UUID4, request: MIPInspectionFormPlagueRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_inspection_form_plague.update(db, request, mip_inspection_form_plague_id)


@router.put('/photos/{mip_inspection_form_photo_id}', status_code=status.HTTP_202_ACCEPTED, response_model=MIPInspectionFormPhotoResponse)
async def update_photo(mip_inspection_form_photo_id: UUID4, request: MIPInspectionFormPhotoRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_inspection_form_photo.update(db, request, mip_inspection_form_photo_id)


@router.delete('/{mip_inspection_form_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(mip_inspection_form_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_inspection_form.delete(db, mip_inspection_form_id)


@router.delete('/plagues/{mip_inspection_form_plague_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy_plague(mip_inspection_form_plague_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_inspection_form_plague.delete(db, mip_inspection_form_plague_id)


@router.delete('/photos/{mip_inspection_form_photo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy_photos(mip_inspection_form_photo_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_inspection_form_photo.delete(db, mip_inspection_form_photo_id)
