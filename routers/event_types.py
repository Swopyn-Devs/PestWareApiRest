from fastapi import APIRouter, Depends, status, Query
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import event_type
from schemas.event_type import EventTypeRequest, EventTypeUpdateRequest, EventTypeResponse

router = APIRouter(
    prefix='/event-types',
    tags=['🏢 Tipos de evento']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[EventTypeResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return event_type.get_all(db, authorize, paginate)


@router.get('/{event_type_id}', status_code=status.HTTP_200_OK, response_model=EventTypeResponse)
async def show(event_type_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return event_type.retrieve(db, event_type_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=EventTypeResponse)
async def store(request: EventTypeRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return event_type.create(db, request, authorize)


@router.put('/{event_type_id}', status_code=status.HTTP_202_ACCEPTED, response_model=EventTypeResponse)
async def update(event_type_id: UUID4, request: EventTypeUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return event_type.update(db, request, event_type_id)


@router.delete('/{event_type_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(event_type_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return event_type.delete(db, event_type_id)
