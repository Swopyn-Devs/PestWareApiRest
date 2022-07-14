from typing import Optional, Union
from pydantic import BaseModel, UUID4, Field
from documentation.service_types import *
from schemas.job_center import JobCenterResponse, JobCenterBasicResponse
from schemas.indication import IndicationResponse, IndicationBasicResponse


class ServiceTypeRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    frequency_days: int = Field(title=title_frequency_days, description=desc_frequency_days, example=ex_frequency_days, ge=0)
    certificate_expiration_days: int = Field(title=title_certificate_expiration_days, description=desc_certificate_expiration_days, example=ex_certificate_expiration_days, ge=0)
    follow_up_days: int = Field(title=title_follow_up_days, description=desc_follow_up_days, example=ex_follow_up_days, ge=0)
    disinfection: Optional[bool] = Field(title=title_disinfection, description=desc_disinfection, example=ex_disinfection)
    show_price: Optional[bool] = Field(title=title_show_price, description=desc_show_price, example=ex_show_price)
    indication_id: UUID4 = Field(title=title_indication_id, description=desc_indication_id, example=ex_indication_id)

    class Config:
        orm_mode = True


class ServiceTypeUpdateRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    frequency_days: int = Field(title=title_frequency_days, description=desc_frequency_days, example=ex_frequency_days, ge=0)
    certificate_expiration_days: int = Field(title=title_certificate_expiration_days, description=desc_certificate_expiration_days, example=ex_certificate_expiration_days, ge=0)
    follow_up_days: int = Field(title=title_follow_up_days, description=desc_follow_up_days, example=ex_follow_up_days, ge=0)
    disinfection: bool = Field(title=title_disinfection, description=desc_disinfection, example=ex_disinfection)
    show_price: Optional[bool] = Field(title=title_show_price, description=desc_show_price, example=ex_show_price)
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
    show_price: bool = Field(title=title_show_price, description=desc_show_price, example=ex_show_price)
    cover: Optional[str] = None
    indication_id: Union[IndicationResponse, IndicationBasicResponse]
    job_center_id: Union[JobCenterResponse, JobCenterBasicResponse]

    class Config:
        orm_mode = True


class ServiceTypeBasicResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    frequency_days: int = Field(title=title_frequency_days, description=desc_frequency_days, example=ex_frequency_days, ge=0)
    certificate_expiration_days: int = Field(title=title_certificate_expiration_days, description=desc_certificate_expiration_days, example=ex_certificate_expiration_days, ge=0)
    follow_up_days: int = Field(title=title_follow_up_days, description=desc_follow_up_days, example=ex_follow_up_days, ge=0)
    disinfection: bool = Field(title=title_disinfection, description=desc_disinfection, example=ex_disinfection)
    show_price: bool = Field(title=title_show_price, description=desc_show_price, example=ex_show_price)
    cover: Optional[str] = None
    indication_id: UUID4
    job_center_id: UUID4

    class Config:
        orm_mode = True
