import uuid

from decouple import config
from fastapi import HTTPException, status
from fastapi_jwt_auth import AuthJWT
from pydantic import UUID1
from slugify import slugify
from sqlalchemy.orm import Session

from models.company import Company
from models.employee import Employee
from models.user import User
from schemas.auth import LoginResponse, LoginRequest, RegisterRequest, UserResponse, RefreshTokenResponse
from utils.hashing import Hash
from utils.jwt import expires


def login(db: Session, request: LoginRequest, authorize: AuthJWT):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='No se encontraron estas credenciales.')

    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Contraseña invalida.')

    access_token = authorize.create_access_token(subject=user.email, expires_time=expires)
    refresh_token = authorize.create_refresh_token(subject=user.email, expires_time=expires)

    return LoginResponse(access_token=access_token, refresh_token=refresh_token, type='Bearer')


def register(db: Session, request: RegisterRequest):
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

    new_user = User(
        email=request.contact_email,
        password=Hash.bcrypt(request.password),
        confirmation_code=code,
        is_verified=True,
        is_active=True
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Create instance
    slug = slugify(request.company_name)
    new_company = Company(
        name=request.company_name,
        slug=slug,
        contact_name=request.contact_name,
        contact_email=request.contact_email,
        contact_phone=request.contact_phone,
        country_id=request.country_id
    )
    db.add(new_company)
    db.commit()
    db.refresh(new_company)

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

    user = db.query(User).filter(User.id == new_user.id)
    user.update({'employee_id': new_employee.id})
    db.commit()

    company = db.query(Company).filter(Company.id == new_company.id)
    company_id = str(new_company.id)
    folio = company_id.split('-')
    company.update({'folio': folio[0]})
    db.commit()

    return new_company


def confirmation_code(db: Session, code: UUID1):
    user = db.query(User).filter(User.confirmation_code == code).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Código invalido.')

    user.update({'is_verified': True, 'is_active': True})
    db.commit()


def profile(db: Session, authorize: AuthJWT):
    current_user = authorize.get_jwt_subject()
    user = db.query(User).filter(User.email == current_user).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encontró el perfil.')

    employee = db.query(Employee).filter(Employee.id == user.employee_id).first()
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encontró el perfil.')

    return UserResponse(
        id=user.id,
        name=employee.name,
        email=user.email,
        company_id=employee.company_id,
        job_center_id=employee.job_center_id,
        job_title_id=employee.job_title_id,
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
