from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from documentation.auth import *
from repository import user
from schemas.auth import LoginRequest, LoginResponse, RegisterRequest
from schemas.company import CompanyResponse

router = APIRouter(
    prefix='/authentication',
    tags=['🔐 Autenticación']
)


@router.post('/login', response_model=LoginResponse, name=name_login, description=desc_login)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    return user.login(db, request)


@router.post('/register', response_model=CompanyResponse, status_code=status.HTTP_201_CREATED, name=name_register,
             description=desc_register)
def login(request: RegisterRequest, db: Session = Depends(get_db)):
    return user.register(db, request)
