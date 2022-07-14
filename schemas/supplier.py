from typing import Union
from pydantic import BaseModel, UUID4, Field
from documentation.suppliers import *
from schemas.job_center import JobCenterResponse, JobCenterBasicResponse


class SupplierRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    contact_name: str = Field(title=title_contact_name, description=desc_contact_name, example=ex_contact_name, max_length=255, min_length=3)
    address: str = Field(title=title_address, description=desc_address, example=ex_address, max_length=255, min_length=3)
    phone: str = Field(title=title_phone, description=desc_phone, example=ex_phone, max_length=255, min_length=3)
    email: str = Field(title=title_email, description=desc_email, example=ex_email, max_length=255, min_length=3)
    bank: str = Field(title=title_bank, description=desc_bank, example=ex_bank, max_length=255, min_length=3)
    account_holder: str = Field(title=title_account_holder, description=desc_account_holder, example=ex_account_holder, max_length=255, min_length=3)
    account_number: str = Field(title=title_account_number, description=desc_account_number, example=ex_account_number, max_length=255, min_length=3)
    taxpayer_registration: str = Field(title=title_taxpayer_registration, description=desc_taxpayer_registration, example=ex_taxpayer_registration, max_length=255, min_length=10)

    class Config:
        orm_mode = True


class SupplierUpdateRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    contact_name: str = Field(title=title_contact_name, description=desc_contact_name, example=ex_contact_name, max_length=255, min_length=3)
    address: str = Field(title=title_address, description=desc_address, example=ex_address, max_length=255, min_length=3)
    phone: str = Field(title=title_phone, description=desc_phone, example=ex_phone, max_length=255, min_length=3)
    email: str = Field(title=title_email, description=desc_email, example=ex_email, max_length=255, min_length=3)
    bank: str = Field(title=title_bank, description=desc_bank, example=ex_bank, max_length=255, min_length=3)
    account_holder: str = Field(title=title_account_holder, description=desc_account_holder, example=ex_account_holder, max_length=255, min_length=3)
    account_number: str = Field(title=title_account_number, description=desc_account_number, example=ex_account_number, max_length=255, min_length=3)
    taxpayer_registration: str = Field(title=title_taxpayer_registration, description=desc_taxpayer_registration, example=ex_taxpayer_registration, max_length=255, min_length=10)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True


class SupplierResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    contact_name: str = Field(title=title_contact_name, description=desc_contact_name, example=ex_contact_name, max_length=255, min_length=3)
    address: str = Field(title=title_address, description=desc_address, example=ex_address, max_length=255, min_length=3)
    phone: str = Field(title=title_phone, description=desc_phone, example=ex_phone, max_length=255, min_length=3)
    email: str = Field(title=title_email, description=desc_email, example=ex_email, max_length=255, min_length=3)
    bank: str = Field(title=title_bank, description=desc_bank, example=ex_bank, max_length=255, min_length=3)
    account_holder: str = Field(title=title_account_holder, description=desc_account_holder, example=ex_account_holder, max_length=255, min_length=3)
    account_number: str = Field(title=title_account_number, description=desc_account_number, example=ex_account_number, max_length=255, min_length=3)
    taxpayer_registration: str = Field(title=title_taxpayer_registration, description=desc_taxpayer_registration, example=ex_taxpayer_registration, max_length=255, min_length=10)
    job_center_id: Union[JobCenterResponse, JobCenterBasicResponse]

    class Config:
        orm_mode = True
