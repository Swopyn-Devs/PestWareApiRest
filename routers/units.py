from fastapi import APIRouter, Depends, status, Query
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import unit
from schemas.unit import UnitRequest, UnitUpdateRequest, UnitResponse

router = APIRouter(
    prefix='/units',
    tags=['⚖️ Unidades']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[UnitResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return unit.get_all(db, authorize, paginate)


@router.get('/{unit_id}', status_code=status.HTTP_200_OK, response_model=UnitResponse)
async def show(unit_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return unit.retrieve(db, unit_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=UnitResponse)
async def store(request: UnitRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return unit.create(db, request, authorize)


@router.put('/{unit_id}', status_code=status.HTTP_202_ACCEPTED, response_model=UnitResponse)
async def update(unit_id: UUID4, request: UnitUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return unit.update(db, request, unit_id)


@router.delete('/{unit_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(unit_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return unit.delete(db, unit_id)
