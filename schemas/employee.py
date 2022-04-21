from typing import Optional
from pydantic import BaseModel, UUID4, EmailStr, Field
from documentation.employees import *


class EmployeeRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    email: EmailStr = Field(title=title_email, description=desc_email, example=ex_email)
    company_id: UUID4 = Field(title=title_company_id, description=desc_company_id, example=ex_company_id)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)
    job_title_id: UUID4 = Field(title=title_job_title_id, description=desc_job_title_id, example=ex_job_title_id)
    color: Optional[str] = None

    class Config:
        orm_mode = True


class EmployeeResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    company_id: UUID4 = Field(title=title_company_id, description=desc_company_id, example=ex_company_id)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)
    job_title_id: UUID4 = Field(title=title_job_title_id, description=desc_job_title_id, example=ex_job_title_id)
    avatar: Optional[str] = None
    signature: Optional[str] = None
    color: Optional[str] = None

    class Config:
        orm_mode = True
