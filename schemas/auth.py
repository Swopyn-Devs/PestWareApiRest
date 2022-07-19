from decouple import config
from pydantic import BaseModel, EmailStr, UUID4, Field
from typing import Optional
from datetime import datetime

from schemas.job_title import JobTitleResponse
from schemas.job_center import JobCenterResponse
from documentation.company import *


class Settings(BaseModel):
    authjwt_secret_key: str = config('SECRET_KEY')


class LoginRequest(BaseModel):
    email: EmailStr = Field(title='Correo electrónico', example='example@swopyn.com')
    password: str = Field(title='Contraseña', max_length=255, min_length=8, example='1234567890')


class LoginResponse(BaseModel):
    access_token: str = Field(title='JWT', description='Json Web Token', example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9')
    refresh_token: str = Field(title='JWT Refresh', example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ')
    type: str = Field(title='Tipo de token', description='Authorization: Bearer token', example='Bearer')


class RefreshTokenResponse(BaseModel):
    access_token: str = Field(title='JWT', description='Json Web Token', example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9')
    type: str = Field(title='Tipo de token', description='Authorization: Bearer token', example='Bearer')


class RegisterRequest(BaseModel):
    company_name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    contact_name: str = Field(title=title_c_name, description=desc_c_name, max_length=255, example=ex_c_name)
    contact_email: EmailStr
    contact_phone: str = Field(title=title_c_phone, description=desc_c_phone, example=ex_c_phone)
    country_id: UUID4 = Field(title=title_country, description=desc_country, example=ex_country)
    password: str = Field(title='Contraseña', max_length=255, min_length=8, example='1234567890')

    class Config:
        orm_mode = True


class RegisterResponse(BaseModel):
    detail: str


class UserResponse(BaseModel):
    id: UUID4
    name: str
    email: EmailStr = Field(title='Correo electrónico', example='example@swopyn.com')
    company_id: UUID4
    job_center: JobCenterResponse
    job_title: JobTitleResponse
    employee_id: UUID4
    avatar: Optional[str] = None
    signature: Optional[str] = None
    color: Optional[str] = None
    is_verified: bool
    device_token: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class ProfileRequest(BaseModel):
    name: Optional[str] = Field(description='Nombre del usuario.', max_length=255, example=ex_c_name)
    email: Optional[EmailStr] = Field(description='El correo debe ser único.', example='example@swopyn.com')
    password: Optional[str] = Field(title='Contraseña', max_length=255, min_length=8, example='1234567890')
    device_token: Optional[str] = Field(title='Token Firebase')


class VerifyAccountRequest(BaseModel):
    confirmation_code: str = Field(title='Código de confirmación',
                                   description='El código es enviado por correo al usuario.', max_length=8,
                                   min_length=8, example='7d19cfe4')


class SendCodeConfirmation(BaseModel):
    email: EmailStr = Field(description='El correo debe ser con el que se registro.', example='example@swopyn.com')
