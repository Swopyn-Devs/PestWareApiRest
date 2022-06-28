from fastapi import APIRouter, Depends, status, Query
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import business_activity
from schemas.business_activity import BusinessActivityRequest, BusinessActivityUpdateRequest, BusinessActivityResponse

router = APIRouter(
    prefix='/business-activities',
    tags=['🏢 Giros de la empresa']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[BusinessActivityResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return business_activity.get_all(db, authorize, paginate)


@router.get('/{business_activity_id}', status_code=status.HTTP_200_OK, response_model=BusinessActivityResponse)
async def show(business_activity_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return business_activity.retrieve(db, business_activity_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=BusinessActivityResponse)
async def store(request: BusinessActivityRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return business_activity.create(db, request, authorize)


@router.put('/{business_activity_id}', status_code=status.HTTP_202_ACCEPTED, response_model=BusinessActivityResponse)
async def update(business_activity_id: UUID4, request: BusinessActivityUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return business_activity.update(db, request, business_activity_id)


@router.delete('/{business_activity_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(business_activity_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return business_activity.delete(db, business_activity_id)
