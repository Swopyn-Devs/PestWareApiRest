from pydantic import BaseModel, UUID4, Field
from typing import Optional
from documentation.quotes import *


class QuoteRequest(BaseModel):
    total: float = Field(title=title_total, description=desc_total, example=ex_total)
    description: Optional[str] = Field(title=title_description, description=desc_description, example=ex_description)
    service_type_id: UUID4 = Field(title=title_service_type_id, description=desc_service_type_id, example=ex_service_type_id)
    customer_id: UUID4 = Field(title=title_customer_id, description=desc_customer_id, example=ex_customer_id)
    origin_source_id: UUID4 = Field(title=title_origin_source_id, description=desc_origin_source_id, example=ex_origin_source_id)
    employee_id: UUID4 = Field(title=title_employee_id, description=desc_employee_id, example=ex_employee_id)

    class Config:
        orm_mode = True


class QuoteUpdateRequest(BaseModel):
    total: float = Field(title=title_total, description=desc_total, example=ex_total)
    description: Optional[str] = Field(title=title_description, description=desc_description, example=ex_description)
    service_type_id: UUID4 = Field(title=title_service_type_id, description=desc_service_type_id, example=ex_service_type_id)
    customer_id: UUID4 = Field(title=title_customer_id, description=desc_customer_id, example=ex_customer_id)
    origin_source_id: UUID4 = Field(title=title_origin_source_id, description=desc_origin_source_id, example=ex_origin_source_id)
    employee_id: UUID4 = Field(title=title_employee_id, description=desc_employee_id, example=ex_employee_id)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True


class QuoteResponse(BaseModel):
    id: UUID4
    total: float = Field(title=title_total, description=desc_folio, example=ex_folio)
    folio: str = Field(title=title_folio, description=desc_total, example=ex_total)
    description: Optional[str] = None
    service_type_id: UUID4 = Field(title=title_service_type_id, description=desc_service_type_id, example=ex_service_type_id)
    customer_id: UUID4 = Field(title=title_customer_id, description=desc_customer_id, example=ex_customer_id)
    origin_source_id: UUID4 = Field(title=title_origin_source_id, description=desc_origin_source_id, example=ex_origin_source_id)
    employee_id: UUID4 = Field(title=title_employee_id, description=desc_employee_id, example=ex_employee_id)
    status_id: UUID4 = Field(title=title_status_id, description=desc_status_id, example=ex_status_id)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True
