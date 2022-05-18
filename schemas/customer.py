from typing import Optional
from datetime import datetime

from pydantic import BaseModel, UUID4, EmailStr


class CustomerRequest(BaseModel):
    name: str
    phone: Optional[str]
    email: Optional[EmailStr]
    contact_name: Optional[str]
    contact_phone: Optional[str]
    contact_email: Optional[str]
    address: Optional[str]
    is_main: bool
    main_customer_id: Optional[UUID4] = None
    job_center_id: UUID4

    class Config:
        orm_mode = True


class CustomerRequestUpdated(BaseModel):
    name: str
    phone: Optional[str]
    email: Optional[EmailStr]
    contact_name: Optional[str]
    contact_phone: Optional[str]
    contact_email: Optional[str]
    address: Optional[str]

    class Config:
        orm_mode = True


class CustomerResponse(BaseModel):
    id: UUID4
    name: str
    folio: str
    phone: Optional[str]
    email: Optional[EmailStr]
    contact_name: Optional[str]
    contact_phone: Optional[str]
    contact_email: Optional[str]
    address: Optional[str]
    is_main: bool
    main_customer_id: Optional[UUID4] = None
    job_center_id: UUID4
    total_branches: int
    total_quotes: int
    total_scheduled_services: int
    total_completed_services: int
    total_canceled_services: int
    quotes_balance: float
    scheduled_services_balance: float
    collected_balance: float
    past_due_balance: float
    is_active: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class CustomerXlsxResponse(BaseModel):
    xlsx_base64: str

    class Config:
        orm_mode = True
