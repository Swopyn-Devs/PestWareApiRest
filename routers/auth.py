from fastapi import APIRouter, Depends, status, BackgroundTasks
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session

from database import get_db
from documentation.auth import *
from repository import user
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

router = APIRouter(
    prefix='/authentication',
    tags=['🔐 Autenticación']
)


@router.post('/login', response_model=LoginResponse, name=name_login, description=desc_login)
def login(request: LoginRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    return user.login(db, request, authorize)


@router.post('/register', response_model=RegisterResponse, status_code=status.HTTP_201_CREATED, name=name_register,
             description=desc_register)
async def register(background_tasks: BackgroundTasks, request: RegisterRequest, db: Session = Depends(get_db)):
    return await user.register(db, request, background_tasks)


@router.post('/verify_account', response_model=LoginResponse, name=name_verify, description=desc_verify)
def verify_account(request: VerifyAccountRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    return user.verify_account(db, request, authorize)


@router.post('/resend_confirmation_code', response_model=RegisterResponse, name=name_send_code,
             description=desc_send_code)
def resend_confirmation_code(background_tasks: BackgroundTasks, request: SendCodeConfirmation,
                             db: Session = Depends(get_db)):
    return user.send_code_confirmation(db, request, background_tasks)


@router.get('/profile', response_model=UserResponse, name=name_profile, description=desc_profile)
def profile(authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    authorize.jwt_required()
    return user.profile(db, authorize)


@router.patch('/profile', response_model=UserResponse, status_code=status.HTTP_202_ACCEPTED, name=name_update,
              description=desc_update)
def profile(request: ProfileRequest, authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    authorize.jwt_required()
    return user.update(db, request, authorize)


@router.post('/refresh_token', response_model=RefreshTokenResponse, name=name_refresh, description=desc_refresh)
def refresh(authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return user.refresh(authorize)
