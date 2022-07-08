from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str = Field(title='Usuario', example='example@swopyn.com')
    password: str = Field(title='Contraseña', max_length=255, min_length=8, example='1234567890')
    job_center_slug: str = Field(title='Slug', description='Parametro de la url del login, es un identificador unico por centro de trabajo.', example='biofin-fumigaciones-organicas')