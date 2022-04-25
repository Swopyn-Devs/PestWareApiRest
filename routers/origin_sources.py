from fastapi import APIRouter, Depends, status, Query
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import origin_source
from schemas.origin_source import OriginSourceRequest, OriginSourceUpdateRequest, OriginSourceResponse

router = APIRouter(
    prefix='/origin-source',
    tags=['🌐 Fuentes de origen']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[OriginSourceResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return origin_source.get_all(db, authorize, paginate)


@router.get('/{origin_source_id}', status_code=status.HTTP_200_OK, response_model=OriginSourceResponse)
async def show(origin_source_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return origin_source.retrieve(db, origin_source_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=OriginSourceResponse)
async def store(request: OriginSourceRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return origin_source.create(db, request, authorize)


@router.put('/{origin_source_id}', status_code=status.HTTP_202_ACCEPTED, response_model=OriginSourceResponse)
async def update(origin_source_id: UUID4, request: OriginSourceUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return origin_source.update(db, request, origin_source_id)


@router.delete('/{origin_source_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(origin_source_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return origin_source.delete(db, origin_source_id)
