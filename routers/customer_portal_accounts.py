from fastapi import APIRouter, Depends, status, Query, BackgroundTasks
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from typing import Optional
from sqlalchemy.orm import Session

from database import get_db
from repository import customer_portal_account
from schemas.customer_portal_account import CustomerPortalAccountRequest, CustomerPortalAccountRequestUpdated, CustomerPortalAccountResponse, SendCredentialsResponse, SendCredentialsRequest

router = APIRouter(
    prefix='/customer/portal-accounts',
    tags=['🔐 Cuentas de portal']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[CustomerPortalAccountResponse])
async def index(customer_id: Optional[UUID4] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return customer_portal_account.get_all(db, authorize, customer_id)


@router.get('/{portal_account_id}', status_code=status.HTTP_200_OK, response_model=CustomerPortalAccountResponse)
async def show(portal_account_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return customer_portal_account.retrieve(db, portal_account_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=CustomerPortalAccountResponse)
async def store(request: CustomerPortalAccountRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return customer_portal_account.create(db, authorize, request)


@router.patch('/{portal_account_id}', status_code=status.HTTP_202_ACCEPTED, response_model=CustomerPortalAccountResponse)
async def update(portal_account_id: UUID4, request: CustomerPortalAccountRequestUpdated, db: Session = Depends(get_db),
                 authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return customer_portal_account.update(db, authorize, request, portal_account_id)


@router.delete('/{portal_account_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(portal_account_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return customer_portal_account.delete(db, portal_account_id)


@router.post('/{portal_account_id}/send_credentials/', response_model=SendCredentialsResponse)
def send_credentials(portal_account_id: UUID4, background_tasks: BackgroundTasks, request: SendCredentialsRequest, db: Session = Depends(get_db)):
    return customer_portal_account.send_credentials(db, portal_account_id, request, background_tasks)
