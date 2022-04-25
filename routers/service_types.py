from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import get_db
from repository import service_type
from schemas.service_type import ServiceTypeRequest, ServiceTypeUpdateRequest, ServiceTypeResponse

router = APIRouter(
    prefix='/service-types',
    tags=['🗂 Tipos de servicio']
)


@router.get('/{paginate}', status_code=status.HTTP_200_OK, response_model=Page[ServiceTypeResponse])
async def index(paginate: bool, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
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
