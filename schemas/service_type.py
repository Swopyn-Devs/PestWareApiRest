from typing import Optional
from pydantic import BaseModel, UUID4, Field
from documentation.service_types import *
from schemas.job_center import JobCenterResponse
from schemas.indication import IndicationResponse


class ServiceTypeRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    frequency_days: int = Field(title=title_frequency_days, description=desc_frequency_days, example=ex_frequency_days, ge=0)
    certificate_expiration_days: int = Field(title=title_certificate_expiration_days, description=desc_certificate_expiration_days, example=ex_certificate_expiration_days, ge=0)
    follow_up_days: int = Field(title=title_follow_up_days, description=desc_follow_up_days, example=ex_follow_up_days, ge=0)
    disinfection: Optional[bool] = Field(title=title_disinfection, description=desc_disinfection, example=ex_disinfection)
    indication_id: UUID4 = Field(title=title_indication_id, description=desc_indication_id, example=ex_indication_id)

    class Config:
        orm_mode = True


class ServiceTypeUpdateRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    frequency_days: int = Field(title=title_frequency_days, description=desc_frequency_days, example=ex_frequency_days, ge=0)
    certificate_expiration_days: int = Field(title=title_certificate_expiration_days, description=desc_certificate_expiration_days, example=ex_certificate_expiration_days, ge=0)
    follow_up_days: int = Field(title=title_follow_up_days, description=desc_follow_up_days, example=ex_follow_up_days, ge=0)
    disinfection: bool = Field(title=title_disinfection, description=desc_disinfection, example=ex_disinfection)
    indication_id: UUID4 = Field(title=title_indication_id, description=desc_indication_id, example=ex_indication_id)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True


class ServiceTypeResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    frequency_days: int = Field(title=title_frequency_days, description=desc_frequency_days, example=ex_frequency_days, ge=0)
    certificate_expiration_days: int = Field(title=title_certificate_expiration_days, description=desc_certificate_expiration_days, example=ex_certificate_expiration_days, ge=0)
    follow_up_days: int = Field(title=title_follow_up_days, description=desc_follow_up_days, example=ex_follow_up_days, ge=0)
    disinfection: bool = Field(title=title_disinfection, description=desc_disinfection, example=ex_disinfection)
    cover: Optional[str] = None
    indication_id: IndicationResponse
    job_center_id: JobCenterResponse

    class Config:
        orm_mode = True
