from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import get_db
from repository import cancellation_reason
from schemas.cancellation_reason import CancellationReasonRequest, CancellationReasonUpdateRequest, CancellationReasonResponse

router = APIRouter(
    prefix='/cancellation-reasons',
    tags=['🚫 Motivos de cancelación']
)


@router.get('/{paginate}', status_code=status.HTTP_200_OK, response_model=Page[CancellationReasonResponse])
async def index(paginate: bool, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return cancellation_reason.get_all(db, authorize, paginate)


@router.get('/{cancellation_reason_id}', status_code=status.HTTP_200_OK, response_model=CancellationReasonResponse)
async def show(cancellation_reason_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return cancellation_reason.retrieve(db, cancellation_reason_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=CancellationReasonResponse)
async def store(request: CancellationReasonRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return cancellation_reason.create(db, request, authorize)


@router.put('/{cancellation_reason_id}', status_code=status.HTTP_202_ACCEPTED, response_model=CancellationReasonResponse)
async def update(cancellation_reason_id: UUID4, request: CancellationReasonUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return cancellation_reason.update(db, request, cancellation_reason_id)


@router.delete('/{cancellation_reason_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(cancellation_reason_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return cancellation_reason.delete(db, cancellation_reason_id)
