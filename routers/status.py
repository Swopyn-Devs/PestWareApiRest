from fastapi import APIRouter, Depends, status, Query
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import status as status_repo
from schemas.status import StatusRequest, StatusResponse

router = APIRouter(
    prefix='/status',
    tags=['💰 Estatus']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[StatusResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return status_repo.get_all(db, authorize, paginate)


@router.get('/{status_id}', status_code=status.HTTP_200_OK, response_model=StatusResponse)
async def show(status_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return status_repo.retrieve(db, status_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=StatusResponse)
async def store(request: StatusRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return status_repo.create(db, request)


@router.put('/{status_id}', status_code=status.HTTP_202_ACCEPTED, response_model=StatusResponse)
async def update(status_id: UUID4, request: StatusRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return status_repo.update(db, request, status_id)


@router.delete('/{status_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(status_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return status_repo.delete(db, status_id)
