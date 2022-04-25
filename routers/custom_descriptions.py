from fastapi import APIRouter, Depends, status, Query
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import custom_description
from schemas.custom_description import CustomDescriptionRequest, CustomDescriptionUpdateRequest, CustomDescriptionResponse

router = APIRouter(
    prefix='/custom-descriptions',
    tags=['📝 Descripciones personalizadas']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[CustomDescriptionResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return custom_description.get_all(db, authorize, paginate)


@router.get('/{custom_description_id}', status_code=status.HTTP_200_OK, response_model=CustomDescriptionResponse)
async def show(custom_description_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return custom_description.retrieve(db, custom_description_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=CustomDescriptionResponse)
async def store(request: CustomDescriptionRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return custom_description.create(db, request, authorize)


@router.put('/{custom_description_id}', status_code=status.HTTP_202_ACCEPTED, response_model=CustomDescriptionResponse)
async def update(custom_description_id: UUID4, request: CustomDescriptionUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return custom_description.update(db, request, custom_description_id)


@router.delete('/{custom_description_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(custom_description_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return custom_description.delete(db, custom_description_id)
