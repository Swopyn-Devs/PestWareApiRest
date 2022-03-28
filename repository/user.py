import uuid

from fastapi import HTTPException, status
from pydantic import UUID1
from slugify import slugify
from sqlalchemy.orm import Session

from models.company import Company
from models.user import User
from schemas.auth import LoginRequest, LoginResponse, RegisterRequest
from utils import jwt
from utils.hashing import Hash


def login(db: Session, request: LoginRequest):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='No se encontraron estas credenciales.')

    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Contraseña invalida.')

    access_token = jwt.create_token(request.dict())

    return LoginResponse(token=access_token, type='bearer')


def register(db: Session, request: RegisterRequest):
    try:
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

        company = db.query(Company).filter(Company.id == new_company.id)
        company_id = str(new_company.id)
        folio = company_id.split('-')
        company.update({'folio': folio[0]})
        db.commit()

        return new_company
    
    except Exception as error:
        print(error)
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error inesperado.')


def confirmation_code(db: Session, code: UUID1):
    user = db.query(User).filter(User.confirmation_code == code).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Código invalido.')

    user.update({'is_verified': True, 'is_active': True})
    db.commit()
