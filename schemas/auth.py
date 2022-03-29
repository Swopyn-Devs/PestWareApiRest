from pydantic import BaseModel, EmailStr, UUID4, Field


class LoginRequest(BaseModel):
    email: EmailStr = Field(title='Correo electrónico', example='example@swopyn.com')
    password: str = Field(title='Contraseña', max_length=255, min_length=8, example='1234567890')


class LoginResponse(BaseModel):
    token: str = Field(title='JWT', description='Json Web Token', example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9')
    type: str = Field(title='Tipo de token', description='Authorization: Bearer token', example='bearer')


class RegisterRequest(BaseModel):
    company_name: str
    contact_name: str
    contact_email: EmailStr
    contact_phone: str
    country_id: UUID4
    password: str

    class Config:
        orm_mode = True


class RegisterResponse(BaseModel):
    detail: str
