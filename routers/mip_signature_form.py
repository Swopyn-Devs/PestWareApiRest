from fastapi import APIRouter, Depends, status, Query, UploadFile
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional, List

from database import get_db
from repository import mip_signature_form
from schemas.mip_signature_form import MIPSignatureFormRequest, MIPSignatureFormResponse

router = APIRouter(
    prefix='/mip-signature-form',
    tags=['🖋 Formulario de firma MIP']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[MIPSignatureFormResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_signature_form.get_all(db, authorize, paginate)


@router.get('/{mip_signature_form_id}', status_code=status.HTTP_200_OK, response_model=MIPSignatureFormResponse)
async def show(mip_signature_form_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_signature_form.retrieve(db, mip_signature_form_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=MIPSignatureFormResponse)
async def store(request: MIPSignatureFormRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_signature_form.create(db, request)


@router.put('/{mip_signature_form_id}', status_code=status.HTTP_202_ACCEPTED, response_model=MIPSignatureFormResponse)
async def update(mip_signature_form_id: UUID4, request: MIPSignatureFormRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_signature_form.update(db, request, mip_signature_form_id)


@router.patch('/{mip_signature_form_id}/signature', status_code=status.HTTP_202_ACCEPTED, response_model=MIPSignatureFormResponse)
async def update_signature(mip_signature_form_id: UUID4, file: UploadFile, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_signature_form.update_signature(db, file, mip_signature_form_id)


@router.delete('/{mip_signature_form_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(mip_signature_form_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return mip_signature_form.delete(db, mip_signature_form_id)
