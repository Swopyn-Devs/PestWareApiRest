from fastapi import APIRouter, Depends, status, Query
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import nesting_area
from schemas.nesting_area import NestingAreaRequest, NestingAreaResponse

router = APIRouter(
    prefix='/nesting-areas',
    tags=['🕸 Áreas de anidación']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[NestingAreaResponse])
async def index(customer_id: Optional[UUID4] = Query(None), paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return nesting_area.get_all(db, authorize, paginate, customer_id)


@router.get('/{nesting_area_id}', status_code=status.HTTP_200_OK, response_model=NestingAreaResponse)
async def show(nesting_area_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return nesting_area.retrieve(db, nesting_area_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=NestingAreaResponse)
async def store(request: NestingAreaRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return nesting_area.create(db, request)


@router.put('/{nesting_area_id}', status_code=status.HTTP_202_ACCEPTED, response_model=NestingAreaResponse)
async def update(nesting_area_id: UUID4, request: NestingAreaRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return nesting_area.update(db, request, nesting_area_id)


@router.delete('/{nesting_area_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(nesting_area_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return nesting_area.delete(db, nesting_area_id)
