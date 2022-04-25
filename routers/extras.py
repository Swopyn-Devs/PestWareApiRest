from fastapi import APIRouter, Depends, status, Query
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import extra
from schemas.extra import ExtraRequest, ExtraUpdateRequest, ExtraResponse

router = APIRouter(
    prefix='/extras',
    tags=['📂 Extras']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[ExtraResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return extra.get_all(db, authorize, paginate)


@router.get('/{extra_id}', status_code=status.HTTP_200_OK, response_model=ExtraResponse)
async def show(extra_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return extra.retrieve(db, extra_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=ExtraResponse)
async def store(request: ExtraRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return extra.create(db, request, authorize)


@router.put('/{extra_id}', status_code=status.HTTP_202_ACCEPTED, response_model=ExtraResponse)
async def update(extra_id: UUID4, request: ExtraUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return extra.update(db, request, extra_id)


@router.delete('/{extra_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(extra_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return extra.delete(db, extra_id)
