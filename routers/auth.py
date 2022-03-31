from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database import get_db
from documentation.auth import *
from repository import user
from schemas.auth import LoginResponse, RegisterRequest, UserResponse, RefreshTokenResponse
from schemas.company import CompanyResponse
from utils.jwt import oauth2_schema

router = APIRouter(
    prefix='/authentication',
    tags=['🔐 Autenticación']
)


@router.post('/login', response_model=LoginResponse, name=name_login, description=desc_login)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return user.login(db, request)


@router.post('/register', response_model=CompanyResponse, status_code=status.HTTP_201_CREATED, name=name_register,
             description=desc_register)
def login(request: RegisterRequest, db: Session = Depends(get_db)):
    return user.register(db, request)


@router.get('/profile', response_model=UserResponse, name=name_profile, description=desc_profile)
def profile(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    return user.profile(db, token)


@router.post('/refresh-token', response_model=RefreshTokenResponse, name=name_refresh, description=desc_refresh)
def refresh():
    return user.refresh()
