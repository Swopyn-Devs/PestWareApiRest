import uuid

from decouple import config
from fastapi import HTTPException, status, BackgroundTasks
from fastapi_jwt_auth import AuthJWT
from fastapi_mail import FastMail, MessageSchema
from sqlalchemy.orm import Session

from models.customer_portal_account import CustomerPortalAccount
from schemas.customer_portal_account import CustomerPortalAccountRequest
from services import mail
from utils.hashing import Hash



from fastapi import HTTPException, status
from fastapi_pagination import paginate
from fastapi_jwt_auth import AuthJWT
from pydantic import UUID4
from sqlalchemy.orm import Session

from utils import functions


model_name = 'cuenta de portal'


def get_all(db: Session, authorize: AuthJWT, customer_id):
    employee = functions.get_employee_id_by_token(db, authorize)
    data = []
    portal_accounts = db.query(CustomerPortalAccount).filter(CustomerPortalAccount.job_center_id == employee.job_center_id).filter(CustomerPortalAccount.is_deleted == False)
    if customer_id is not None:
        portal_accounts = portal_accounts.filter(CustomerPortalAccount.customer_id == customer_id)

    return paginate(data)


def retrieve(db: Session, portal_account_id: UUID4):
    account = db.query(CustomerPortalAccount).filter(CustomerPortalAccount.id == portal_account_id).filter(CustomerPortalAccount.is_deleted == False).first()
    if not account:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'La cuenta de portal con el id {portal_account_id} no esta disponible.')

    return account


def create(db: Session, authorize: AuthJWT, request: CustomerPortalAccountRequest):
    employee = functions.get_employee_id_by_token(db, authorize)
    account = db.query(CustomerPortalAccount).filter(CustomerPortalAccount.job_center_id == employee.job_center_id).filter(CustomerPortalAccount.is_deleted == False).filter(CustomerPortalAccount.username == request.username).first()

    if account:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Ya existe una cuenta con este usuario.')

    new_account = CustomerPortalAccount(
        name=request.name,
        username=request.username,
        password=Hash.bcrypt(request.password),
        customer_id=request.customer_id,
        is_active=True
    )

    db.add(new_account)
    db.commit()
    db.refresh(new_account)

    return new_account


def update(db: Session, request: CustomerPortalAccountRequest, portal_account_id: UUID4):
    account = db.query(CustomerPortalAccount).filter(CustomerPortalAccount.id == portal_account_id).filter(CustomerPortalAccount.is_deleted == False)
    if not account.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'La cuenta de portal con el id {portal_account_id} no esta disponible.')

    account.update(request.dict())
    db.commit()

    if request.password is not None:
        account.update({'password': Hash.bcrypt(request.password)})
        db.commit()

    return account.first()


def delete(db: Session, portal_account_id: UUID4):
    account = db.query(CustomerPortalAccount).filter(CustomerPortalAccount.id == portal_account_id)
    if not account.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'La cuenta de portal con el id {portal_account_id} no esta disponible.')

    account.update({'is_deleted': True})
    db.commit()

    return {'detail': 'La cuenta de portal se elimino correctamente.'}
