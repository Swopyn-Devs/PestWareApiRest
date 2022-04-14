from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import get_db
from repository import application_method
from schemas.application_method import ApplicationMethodRequest, ApplicationMethodUpdateRequest, ApplicationMethodResponse

router = APIRouter(
    prefix='/application-methods',
    tags=['📋  Métodos de aplicación']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[ApplicationMethodResponse])
async def index(db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return application_method.get_all(db, authorize)


@router.get('/{application_method_id}', status_code=status.HTTP_200_OK, response_model=ApplicationMethodResponse)
async def show(application_method_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return application_method.retrieve(db, application_method_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=ApplicationMethodResponse)
async def store(request: ApplicationMethodRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return application_method.create(db, request, authorize)


@router.put('/{application_method_id}', status_code=status.HTTP_202_ACCEPTED, response_model=ApplicationMethodResponse)
async def update(application_method_id: UUID4, request: ApplicationMethodUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return application_method.update(db, request, application_method_id)


@router.delete('/{application_method_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(application_method_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return application_method.delete(db, application_method_id)
