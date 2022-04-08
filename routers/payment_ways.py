from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import get_db
from repository import payment_way
from schemas.payment_way import PaymentWayRequest, PaymentWayResponse

router = APIRouter(
    prefix='/payment-ways',
    tags=['💵 Formas de pago']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[PaymentWayResponse])
async def index(db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return payment_way.get_all(db)


@router.get('/{payment_way_id}', status_code=status.HTTP_200_OK, response_model=PaymentWayResponse)
async def show(payment_way_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return payment_way.retrieve(db, payment_way_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=PaymentWayResponse)
async def store(request: PaymentWayRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return payment_way.create(db, request)


@router.put('/{payment_way_id}', status_code=status.HTTP_202_ACCEPTED, response_model=PaymentWayResponse)
async def update(payment_way_id: UUID4, request: PaymentWayRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return payment_way.update(db, request, payment_way_id)


@router.delete('/{payment_way_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(payment_way_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return payment_way.delete(db, payment_way_id)
