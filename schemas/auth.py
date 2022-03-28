from pydantic import BaseModel, EmailStr, UUID4


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    token: str
    type: str


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
