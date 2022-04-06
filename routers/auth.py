from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session

from database import get_db
from documentation.auth import *
from repository import user
from schemas.auth import LoginResponse, LoginRequest, RegisterRequest, UserResponse, RefreshTokenResponse
from schemas.company import CompanyResponse

router = APIRouter(
    prefix='/authentication',
    tags=['🔐 Autenticación']
)


@router.post('/login', response_model=LoginResponse, name=name_login, description=desc_login)
def login(request: LoginRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    return user.login(db, request, authorize)


@router.post('/register', response_model=CompanyResponse, status_code=status.HTTP_201_CREATED, name=name_register,
             description=desc_register)
def login(request: RegisterRequest, db: Session = Depends(get_db)):
    return user.register(db, request)


@router.get('/profile', response_model=UserResponse, name=name_profile, description=desc_profile)
def profile(authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    authorize.jwt_required()
    return user.profile(db, authorize)


@router.post('/refresh_token', response_model=RefreshTokenResponse, name=name_refresh, description=desc_refresh)
def refresh(authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return user.refresh(authorize)
