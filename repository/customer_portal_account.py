import uuid

from decouple import config
from fastapi import HTTPException, status, BackgroundTasks
from fastapi_jwt_auth import AuthJWT
from fastapi_mail import FastMail, MessageSchema
from sqlalchemy.orm import Session

from models.job_center import JobCenter
from models.customer import Customer
from models.customer_portal_account import CustomerPortalAccount
from schemas.auth import LoginResponse
from schemas.auth_customer import LoginRequest
from schemas.customer_portal_account import CustomerPortalAccountRequest, CustomerPortalAccountRequestUpdated, SendCredentialsRequest, SendCredentialsResponse
from services import mail
from utils.jwt import expires
from utils.hashing import Hash


from fastapi_pagination import paginate
from fastapi_jwt_auth import AuthJWT
from pydantic import UUID4
from sqlalchemy.orm import Session

from utils import functions


model_name = 'cuenta de portal'


def get_all(db: Session, authorize: AuthJWT, customer_id):
    employee = functions.get_employee_id_by_token(db, authorize)
    portal_accounts = db.query(CustomerPortalAccount).\
        join(Customer, CustomerPortalAccount.customer_id == Customer.id).\
        filter(Customer.job_center_id == employee.job_center_id).filter(CustomerPortalAccount.is_deleted == False)
    if customer_id is not None:
        portal_accounts = portal_accounts.filter(CustomerPortalAccount.customer_id == customer_id)

    return paginate(portal_accounts.all())


def retrieve(db: Session, portal_account_id: UUID4):
    account = db.query(CustomerPortalAccount).filter(CustomerPortalAccount.id == portal_account_id).filter(CustomerPortalAccount.is_deleted == False).first()
    if not account:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'La cuenta de portal con el id {portal_account_id} no esta disponible.')

    return account


def create(db: Session, authorize: AuthJWT, request: CustomerPortalAccountRequest):
    employee = functions.get_employee_id_by_token(db, authorize)
    account = db.query(CustomerPortalAccount).\
        join(Customer, CustomerPortalAccount.customer_id == Customer.id).\
        filter(Customer.job_center_id == employee.job_center_id).filter(CustomerPortalAccount.is_deleted == False).\
        filter(CustomerPortalAccount.username == request.username).first()

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


def update(db: Session, authorize: AuthJWT, request: CustomerPortalAccountRequestUpdated, portal_account_id: UUID4):
    employee = functions.get_employee_id_by_token(db, authorize)
    account = db.query(CustomerPortalAccount).filter(CustomerPortalAccount.id == portal_account_id).filter(CustomerPortalAccount.is_deleted == False)
    if not account.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'La cuenta de portal con el id {portal_account_id} no esta disponible.')

    if request.username is not None:
        account_portal = db.query(CustomerPortalAccount).\
            join(Customer, CustomerPortalAccount.customer_id == Customer.id).\
            filter(Customer.job_center_id == employee.job_center_id).filter(CustomerPortalAccount.is_deleted == False).\
            filter(CustomerPortalAccount.id != portal_account_id).\
            filter(CustomerPortalAccount.username == request.username).first()

        if account_portal:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        detail='Ya existe una cuenta con este usuario.')

        account.update({'username': request.username})
        db.commit()


    if request.name is not None:
        account.update({'name': request.name})
        db.commit()

    if request.is_active is not None:
        account.update({'is_active': request.is_active})
        db.commit()

    if request.customer_id is not None:
        account.update({'customer_id': request.customer_id})
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


def send_credentials(db: Session, portal_account_id: UUID4, request: SendCredentialsRequest, background_tasks: BackgroundTasks):
    account = db.query(CustomerPortalAccount).filter(CustomerPortalAccount.id == portal_account_id).first()
    if not account:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'La cuenta de portal con el id {portal_account_id} no esta disponible.')

    # Get credentials account and send by email.
    conf = mail.conf
    data = {'name': account.name, 'username': account.username, 'password': account.password}

    message = MessageSchema(
        subject="Credenciales Portal Clientes",
        recipients=[request.email],
        template_body=data,
        subtype='html'
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message, template_name='mail_welcome_portal.html')

    return SendCredentialsResponse(detail='Se ha enviado las credenciales de acceso a la cuenta de correo del cliente.')


def login(db: Session, request: LoginRequest, authorize: AuthJWT):
    job_center = db.query(JobCenter).filter(JobCenter.slug == request.job_center_slug).first()
    if not job_center:
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='La url de esta página es incorrecta.')

    user = db.query(CustomerPortalAccount).\
            join(Customer, CustomerPortalAccount.customer_id == Customer.id).\
            filter(Customer.job_center_id == job_center.id).filter(CustomerPortalAccount.is_deleted == False).\
            filter(CustomerPortalAccount.username == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='No se encontraron estas credenciales.')

    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Contraseña invalida.')

    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Tu cuenta esta suspendida.')

    access_token = authorize.create_access_token(subject=str(user.id), expires_time=expires)
    refresh_token = authorize.create_refresh_token(subject=str(user.id), expires_time=expires)

    return LoginResponse(access_token=access_token, refresh_token=refresh_token, type='Bearer')
