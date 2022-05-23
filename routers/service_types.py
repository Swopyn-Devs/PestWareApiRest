from fastapi import APIRouter, Depends, status, Query, UploadFile
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import service_type
from schemas.service_type import ServiceTypeRequest, ServiceTypeUpdateRequest, ServiceTypeResponse

router = APIRouter(
    prefix='/service-types',
    tags=['🗂 Tipos de servicio']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[ServiceTypeResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return service_type.get_all(db, authorize, paginate)


@router.get('/{service_type_id}', status_code=status.HTTP_200_OK, response_model=ServiceTypeResponse)
async def show(service_type_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return service_type.retrieve(db, service_type_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=ServiceTypeResponse)
async def store(request: ServiceTypeRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return service_type.create(db, request, authorize)


@router.put('/{service_type_id}', status_code=status.HTTP_202_ACCEPTED, response_model=ServiceTypeResponse)
async def update(service_type_id: UUID4, request: ServiceTypeUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return service_type.update(db, request, service_type_id)


@router.delete('/{service_type_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(service_type_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return service_type.delete(db, service_type_id)


@router.patch('/{service_type_id}/cover', status_code=status.HTTP_202_ACCEPTED, response_model=ServiceTypeResponse)
async def update_cover(service_type_id: UUID4, file: UploadFile, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return service_type.update_cover(db, file, service_type_id)


@router.delete('/{service_type_id}/cover', status_code=status.HTTP_202_ACCEPTED, response_model=ServiceTypeResponse)
async def delete_cover(service_type_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return service_type.delete_cover(db, service_type_id)
