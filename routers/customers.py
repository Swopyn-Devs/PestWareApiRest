from fastapi import APIRouter, Depends, status, Query
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from typing import Optional
from sqlalchemy.orm import Session

from database import get_db
from repository import customer
from schemas.customer import CustomerRequest, CustomerRequestUpdated, CustomerResponse

router = APIRouter(
    prefix='/customers',
    tags=['🏢 Clientes']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[CustomerResponse])
async def index(
        is_main: Optional[bool] = Query(None),
        main_customer: Optional[UUID4] = Query(None),
        folio: Optional[str] = Query(None),
        name: Optional[str] = Query(None),
        is_active: Optional[bool] = Query(None),
        contact: Optional[str] = Query(None),
        db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return customer.get_all(db, authorize, is_main, main_customer, folio, name, is_active, contact)


@router.get('/{customer_id}', status_code=status.HTTP_200_OK, response_model=CustomerResponse)
async def show(customer_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return customer.retrieve(db, customer_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=CustomerResponse)
async def store(request: CustomerRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return customer.create(db, request)


@router.put('/{customer_id}', status_code=status.HTTP_202_ACCEPTED, response_model=CustomerResponse)
async def update(customer_id: UUID4, request: CustomerRequestUpdated, db: Session = Depends(get_db),
                 authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return customer.update(db, request, customer_id)


@router.delete('/{customer_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(customer_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return customer.delete(db, customer_id)
