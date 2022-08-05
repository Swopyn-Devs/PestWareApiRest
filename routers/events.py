from fastapi import APIRouter, Depends, status, Query
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import event
from schemas.event import EventRequest, EventResponse

router = APIRouter(
    prefix='/events',
    tags=['📆 Eventos de Agenda']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[EventResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return event.get_all(db, authorize, paginate)


@router.get('/{event_id}', status_code=status.HTTP_200_OK, response_model=EventResponse)
async def show(event_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return event.retrieve(db, event_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=EventResponse)
async def store(request: EventRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return event.create(db, request, authorize)


@router.put('/{event_id}', status_code=status.HTTP_202_ACCEPTED, response_model=EventResponse)
async def update(event_id: UUID4, request: EventRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return event.update(db, request, event_id)


@router.delete('/{event_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(event_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return event.delete(db, event_id)
