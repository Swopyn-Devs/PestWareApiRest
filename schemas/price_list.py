from typing import Optional
from pydantic import BaseModel, UUID4, Field
from documentation.price_lists import *


class PriceListRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    key: str = Field(title=title_key, description=desc_key, max_length=255, min_length=3, example=ex_key)
    hierarchy: int = Field(title=title_hierarchy, description=desc_hierarchy, example=ex_hierarchy, ge=1)
    cost: float = Field(title=title_cost, description=desc_cost, example=ex_cost, ge=1)
    frequency_days: int = Field(title=title_frequency_days, description=desc_frequency_days, example=ex_frequency_days, ge=0)
    certificate_expiration_days: int = Field(title=title_certificate_expiration_days, description=desc_certificate_expiration_days, example=ex_certificate_expiration_days, ge=0)
    show_price: Optional[bool] = Field(title=title_show_price, description=desc_show_price, example=ex_show_price)
    disinfection: Optional[bool] = Field(title=title_disinfection, description=desc_disinfection, example=ex_disinfection)
    service_type_id: UUID4 = Field(title=title_service_type_id, description=desc_service_type_id, example=ex_service_type_id)
    indication_id: UUID4 = Field(title=title_indication_id, description=desc_indication_id, example=ex_indication_id)

    class Config:
        orm_mode = True


class PriceListResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    key: str = Field(title=title_key, description=desc_key, max_length=255, min_length=3, example=ex_key)
    hierarchy: int = Field(title=title_hierarchy, description=desc_hierarchy, example=ex_hierarchy, ge=1)
    cost: float = Field(title=title_cost, description=desc_cost, example=ex_cost, ge=1)
    frequency_days: int = Field(title=title_frequency_days, description=desc_frequency_days, example=ex_frequency_days, ge=0)
    certificate_expiration_days: int = Field(title=title_certificate_expiration_days, description=desc_certificate_expiration_days, example=ex_certificate_expiration_days, ge=0)
    show_price: bool = Field(title=title_show_price, description=desc_show_price, example=ex_show_price)
    disinfection: bool = Field(title=title_disinfection, description=desc_disinfection, example=ex_disinfection)
    cover: Optional[str] = None
    service_type_id: UUID4 = Field(title=title_service_type_id, description=desc_service_type_id, example=ex_service_type_id)
    indication_id: UUID4 = Field(title=title_indication_id, description=desc_indication_id, example=ex_indication_id)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True
