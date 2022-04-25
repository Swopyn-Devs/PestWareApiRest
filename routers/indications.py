from fastapi import APIRouter, Depends, status, Query
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import indication
from schemas.indication import IndicationRequest, IndicationUpdateRequest, IndicationResponse

router = APIRouter(
    prefix='/indications',
    tags=['💬 Indicaciones']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[IndicationResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return indication.get_all(db, authorize, paginate)


@router.get('/{indication_id}', status_code=status.HTTP_200_OK, response_model=IndicationResponse)
async def show(indication_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return indication.retrieve(db, indication_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=IndicationResponse)
async def store(request: IndicationRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return indication.create(db, request, authorize)


@router.put('/{indication_id}', status_code=status.HTTP_202_ACCEPTED, response_model=IndicationResponse)
async def update(indication_id: UUID4, request: IndicationUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return indication.update(db, request, indication_id)


@router.delete('/{indication_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(indication_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return indication.delete(db, indication_id)
