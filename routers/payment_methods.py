from fastapi import APIRouter, Depends, status, Query
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import payment_method
from schemas.payment_method import PaymentMethodRequest, PaymentMethodUpdateRequest, PaymentMethodResponse

router = APIRouter(
    prefix='/payment-methods',
    tags=['💳 Métodos de pago']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[PaymentMethodResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return payment_method.get_all(db, authorize, paginate)


@router.get('/{payment_method_id}', status_code=status.HTTP_200_OK, response_model=PaymentMethodResponse)
async def show(payment_method_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return payment_method.retrieve(db, payment_method_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=PaymentMethodResponse)
async def store(request: PaymentMethodRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return payment_method.create(db, request, authorize)


@router.put('/{payment_method_id}', status_code=status.HTTP_202_ACCEPTED, response_model=PaymentMethodResponse)
async def update(payment_method_id: UUID4, request: PaymentMethodUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return payment_method.update(db, request, payment_method_id)


@router.delete('/{payment_method_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(payment_method_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return payment_method.delete(db, payment_method_id)
