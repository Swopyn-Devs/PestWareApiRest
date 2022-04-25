from fastapi import APIRouter, Depends, status, Query
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import rejection_reason
from schemas.rejection_reason import RejectionReasonRequest, RejectionReasonUpdateRequest, RejectionReasonResponse

router = APIRouter(
    prefix='/rejection-reasons',
    tags=['❌ Motivos de rechazo']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[RejectionReasonResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return rejection_reason.get_all(db, authorize, paginate)


@router.get('/{rejection_reason_id}', status_code=status.HTTP_200_OK, response_model=RejectionReasonResponse)
async def show(rejection_reason_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return rejection_reason.retrieve(db, rejection_reason_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=RejectionReasonResponse)
async def store(request: RejectionReasonRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return rejection_reason.create(db, request, authorize)


@router.put('/{rejection_reason_id}', status_code=status.HTTP_202_ACCEPTED, response_model=RejectionReasonResponse)
async def update(rejection_reason_id: UUID4, request: RejectionReasonUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return rejection_reason.update(db, request, rejection_reason_id)


@router.delete('/{rejection_reason_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(rejection_reason_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return rejection_reason.delete(db, rejection_reason_id)
