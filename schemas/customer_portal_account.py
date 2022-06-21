from datetime import datetime
from typing import Optional
from pydantic import BaseModel, UUID4, Field


class CustomerPortalAccountRequest(BaseModel):
    name: str = Field(title='Nombre', example='Carlos Gaytan')
    username: str = Field(title='Nombre del usuario', description='Puede ser un correo, nickname, teléfono, folio, etc.', example='carlos.gaytan@polloshermanos.com')
    password: str = Field(title='Contraseña', max_length=255, min_length=8, example='1234567890')
    customer_id: UUID4 = Field(title='ID del cliente', description='La cuenta de portal pertenece a un cliente.', example='cbce9d10-7d92-4f21-90ff-0b859aa304b5')

    class Config:
        orm_mode = True


class CustomerPortalAccountRequestUpdated(BaseModel):
    name: Optional[str] = Field(title='Nombre', example='Carlos Gaytan')
    username: Optional[str] = Field(title='Nombre del usuario', description='Puede ser un correo, nickname, teléfono, folio, etc.', example='carlos.gaytan@polloshermanos.com')
    password: Optional[str] = Field(title='Contraseña', max_length=255, min_length=8, example='1234567890')
    customer_id: Optional[UUID4] = Field(title='ID del cliente', description='La cuenta de portal pertenece a un cliente.', example='cbce9d10-7d92-4f21-90ff-0b859aa304b5')

    class Config:
        orm_mode = True


class CustomerPortalAccountResponse(BaseModel):
    id: UUID4 = Field(title='ID del objeto', description='ID de la cuenta', example='cbce9d10-7d92-4f21-90ff-0b859aa304b5')
    name: str = Field(title='Nombre', example='Carlos Gaytan')
    username: str = Field(title='Nombre del usuario', description='Puede ser un correo, nickname, teléfono, folio, etc.', example='carlos.gaytan@polloshermanos.com')
    customer_id: UUID4 = Field(title='ID del cliente', description='La cuenta de portal pertenece a un cliente.', example='cbce9d10-7d92-4f21-90ff-0b859aa304b5')
    is_active: bool
    created_at: datetime
    updated_at: datetime
