from typing import Optional, Union
from datetime import datetime
from pydantic import BaseModel, UUID4, EmailStr
from schemas.job_center import JobCenterResponse, JobCenterBasicResponse
from schemas.business_activity import BusinessActivityResponse, BusinessActivityBasicResponse


class CustomerRequest(BaseModel):
    name: str
    phone: Optional[str]
    email: Optional[EmailStr]
    contact_name: Optional[str]
    contact_phone: Optional[str]
    contact_email: Optional[str]
    address: Optional[str]
    address_latitude: Optional[float] = None
    address_longitude: Optional[float] = None
    is_main: bool
    main_customer_id: Optional[UUID4] = None
    business_activity_id: UUID4
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
    address_latitude: Optional[float] = None
    address_longitude: Optional[float] = None
    business_activity_id: Optional[UUID4] = None

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
    address_latitude: Optional[float] = None
    address_longitude: Optional[float] = None
    is_main: bool
    main_customer_id: Optional[UUID4] = None
    business_activity_id: Union[BusinessActivityResponse, BusinessActivityBasicResponse]
    job_center_id: Union[JobCenterResponse, JobCenterBasicResponse]
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


class CustomerBasicResponse(BaseModel):
    id: UUID4
    name: str
    folio: str
    phone: Optional[str]
    email: Optional[EmailStr]
    contact_name: Optional[str]
    contact_phone: Optional[str]
    contact_email: Optional[str]
    address: Optional[str]
    address_latitude: Optional[float] = None
    address_longitude: Optional[float] = None
    is_main: bool
    main_customer_id: Optional[UUID4] = None
    business_activity_id: UUID4
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
