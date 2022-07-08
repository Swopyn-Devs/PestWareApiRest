from pydantic import BaseModel, UUID4, Field

from documentation.company import *


class LoginRequest(BaseModel):
    username: str = Field(title='Usuario', example='example@swopyn.com')
    password: str = Field(title='Contraseña', max_length=255, min_length=8, example='1234567890')