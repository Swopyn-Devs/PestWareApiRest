from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import get_db
from repository import type
from schemas.type import TypeRequest, TypeUpdateRequest, TypeResponse

router = APIRouter(
    prefix='/types',
    tags=['📑 Tipo de productos']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[TypeResponse])
async def index(db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return type.get_all(db, authorize)


@router.get('/{type_id}', status_code=status.HTTP_200_OK, response_model=TypeResponse)
async def show(type_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return type.retrieve(db, type_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=TypeResponse)
async def store(request: TypeRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return type.create(db, request, authorize)


@router.put('/{type_id}', status_code=status.HTTP_202_ACCEPTED, response_model=TypeResponse)
async def update(type_id: UUID4, request: TypeUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return type.update(db, request, type_id)


@router.delete('/{type_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(type_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return type.delete(db, type_id)
