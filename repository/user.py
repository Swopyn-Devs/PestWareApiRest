import uuid

from decouple import config
from fastapi import HTTPException, status, BackgroundTasks
from fastapi_jwt_auth import AuthJWT
from fastapi_mail import FastMail, MessageSchema
from slugify import slugify
from sqlalchemy.orm import Session

from models.company import Company
from models.employee import Employee
from models.user import User
from schemas.auth import (
    LoginResponse,
    LoginRequest,
    RegisterRequest,
    RegisterResponse,
    VerifyAccountRequest,
    UserResponse,
    RefreshTokenResponse,
    ProfileRequest,
    SendCodeConfirmation
)
import repository.job_title as job_title_repo
import repository.job_center as job_center_repo
from services import mail
from utils.hashing import Hash
from utils.jwt import expires
from services import aws


def login(db: Session, request: LoginRequest, authorize: AuthJWT):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='No se encontraron estas credenciales.')

    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Contraseña invalida.')

    if not user.is_verified:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Tu cuenta no ha sido verificada.')

    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Tu cuenta esta suspendida.')

    access_token = authorize.create_access_token(subject=str(user.id), expires_time=expires)
    refresh_token = authorize.create_refresh_token(subject=str(user.id), expires_time=expires)

    return LoginResponse(access_token=access_token, refresh_token=refresh_token, type='Bearer')


async def register(db: Session, request: RegisterRequest, background_tasks: BackgroundTasks):
    # validated user
    user = db.query(User).filter(User.email == request.contact_email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Ya existe una cuenta con este correo.')

    # validation for verify is not already company name.
    company = db.query(Company).filter(Company.name == request.company_name).first()
    if company:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Ya existe una empresa con este nombre.')

    # Generate confirmation code and send by email.
    code = uuid.uuid1()
    code = str(code).split('-')[0]

    # Create instance
    slug = slugify(request.company_name)
    new_company = Company(
        name=request.company_name,
        slug=slug,
        contact_name=request.contact_name,
        contact_email=request.contact_email,
        contact_phone=request.contact_phone,
        country_id=request.country_id,
        web_color='#3C5898'
    )
    db.add(new_company)
    db.commit()
    db.refresh(new_company)

    # Upload files default to AWS S3
    key_document_logo = f'document_logos/{new_company.id}.jpeg'
    file = 'static/companies/document_logo.jpeg'
    if not aws.upload_default_image(config('AWS_S3_BUCKET_COMPANIES'), key_document_logo, file):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f'No fue posible actualizar el logo para documentos.')

    key_document_stamp = f'document_stamps/{new_company.id}.jpeg'
    file = 'static/companies/document_stamp.jpeg'
    if not aws.upload_default_image(config('AWS_S3_BUCKET_COMPANIES'), key_document_stamp, file):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f'No fue posible actualizar el sello para documentos.')

    key_web_logo = f'web_logos/{new_company.id}.jpeg'
    file = 'static/companies/web_logo.jpeg'
    if not aws.upload_default_image(config('AWS_S3_BUCKET_COMPANIES'), key_web_logo, file):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f'No fue posible actualizar el logo para web.')

    # Create employee
    new_employee = Employee(
        name=request.contact_name,
        company_id=new_company.id,
        job_center_id=new_company.id,
        job_title_id=new_company.id
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    # Upload file to AWS S3
    key = f'avatars/{new_employee.id}.jpeg'
    file = 'static/employees/avatar.jpeg'
    if not aws.upload_default_image(config('AWS_S3_BUCKET_EMPLOYEES'), key, file):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f'No fue posible subir la foto de perfil.')

    employee = db.query(Employee).filter(Employee.id == new_employee.id)
    employee.update({'avatar': key})
    db.commit()

    new_user = User(
        email=request.contact_email,
        password=Hash.bcrypt(request.password),
        confirmation_code=code,
        employee_id=new_employee.id,
        is_verified=False,
        is_active=False
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    company = db.query(Company).filter(Company.id == new_company.id)
    company_id = str(new_company.id)
    folio = company_id.split('-')
    company.update({'folio': folio[0], 'document_logo': key_document_logo, 'document_stamp': key_document_stamp,
                    'web_logo': key_web_logo})
    db.commit()

    conf = mail.conf
    data = {'contact_name': request.contact_name, 'confirmation_code': code}

    message = MessageSchema(
        subject="Confirma tu cuenta",
        recipients=[request.contact_email],
        template_body=data,
        subtype='html'
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message, template_name='mail_verify.html')

    return RegisterResponse(detail='Se ha enviado un código de confirmación a tu cuenta de correo.')


def verify_account(db: Session, request: VerifyAccountRequest, authorize: AuthJWT):
    user = db.query(User).filter(User.confirmation_code == request.confirmation_code)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Código invalido.')

    if user.first().is_verified:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='La cuenta ya esta verificada.')

    user.update({'is_verified': True, 'is_active': True})
    db.commit()

    user_id = str(user.first().id)
    access_token = authorize.create_access_token(subject=user_id, expires_time=expires)
    refresh_token = authorize.create_refresh_token(subject=user_id, expires_time=expires)

    return LoginResponse(access_token=access_token, refresh_token=refresh_token, type='Bearer')


def send_code_confirmation(db: Session, request: SendCodeConfirmation, background_tasks: BackgroundTasks):
    user = db.query(User).filter(User.email == request.email)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encontró una cuenta con este correo.')

    if user.first().is_verified:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='La cuenta ya esta verificada.')

    employee = db.query(Employee).filter(Employee.id == user.first().employee_id).first()
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encontró información de esta cuenta.')

    # Generate confirmation code and send by email.
    code = uuid.uuid1()
    code = str(code).split('-')[0]
    conf = mail.conf
    data = {'contact_name': employee.name, 'confirmation_code': code}

    user.update({'confirmation_code': code})
    db.commit()

    message = MessageSchema(
        subject="Confirma tu cuenta",
        recipients=[request.email],
        template_body=data,
        subtype='html'
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message, template_name='mail_verify.html')

    return RegisterResponse(detail='Se ha enviado un código de confirmación a tu cuenta de correo.')


def profile(db: Session, authorize: AuthJWT):
    current_user = authorize.get_jwt_subject()
    user = db.query(User).filter(User.id == current_user).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encontró el perfil.')

    employee = db.query(Employee).filter(Employee.id == user.employee_id).first()
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encontró el perfil.')

    employee = map_s3_url(employee)
    job_title = job_title_repo.retrieve(db, employee.job_title_id)
    job_center = job_center_repo.retrieve(db, employee.job_center_id)

    return UserResponse(
        id=user.id,
        name=employee.name,
        email=user.email,
        company_id=employee.company_id,
        job_center=job_center,
        job_title=job_title,
        employee_id=employee.id,
        avatar=employee.avatar,
        signature=employee.signature,
        color=employee.color,
        is_verified=user.is_verified,
        is_active=user.is_active,
        created_at=employee.created_at,
        updated_at=employee.updated_at
    )


def update(db: Session, request: ProfileRequest, authorize: AuthJWT):
    current_user = authorize.get_jwt_subject()
    user = db.query(User).filter(User.id == current_user)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encontró el perfil.')

    employee = db.query(Employee).filter(Employee.id == user.first().employee_id)

    if request.name is not None:
        employee.update({'name': request.name})
        db.commit()

    if request.email is not None:
        # validated user
        user_validate = db.query(User).filter(User.email == request.email).filter(User.id != user.first().id).first()
        if user_validate:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                detail='Ya existe una cuenta con este correo.')
        user.update({'email': request.email})
        db.commit()
        user = db.query(User).filter(User.email == request.email)

    if request.password is not None:
        user.update({'password': Hash.bcrypt(request.password)})
        db.commit()

    user = user.first()
    employee = employee.first()
    job_title = job_title_repo.retrieve(db, employee.job_title_id)
    job_center = job_center_repo.retrieve(db, employee.job_center_id)

    return UserResponse(
        id=user.id,
        name=employee.name,
        email=user.email,
        company_id=employee.company_id,
        job_center=job_center,
        job_title=job_title,
        employee_id=employee.id,
        avatar=employee.avatar,
        signature=employee.signature,
        color=employee.color,
        is_verified=user.is_verified,
        is_active=user.is_active,
        created_at=employee.created_at,
        updated_at=employee.updated_at
    )


def refresh(authorize: AuthJWT):
    current_user = authorize.get_jwt_subject()
    new_access_token = authorize.create_access_token(subject=current_user, expires_time=expires)

    RefreshTokenResponse(access_token=new_access_token, type='Bearer')


def map_s3_url(employee: Employee):
    if employee.avatar is not None:
        employee.avatar = f"{config('AWS_S3_URL_EMPLOYEES')}/{employee.avatar}"
    if employee.signature is not None:
        employee.signature = f"{config('AWS_S3_URL_EMPLOYEES')}/{employee.signature}"

    return employee
