from typing import Optional
from pydantic import BaseModel, UUID4, Field
from documentation.price_lists import *
from schemas.job_center import JobCenterResponse
from schemas.service_type import ServiceTypeResponse


class PriceListRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    key: str = Field(title=title_key, description=desc_key, max_length=255, min_length=3, example=ex_key)
    hierarchy: int = Field(title=title_hierarchy, description=desc_hierarchy, example=ex_hierarchy, ge=1)
    cost: float = Field(title=title_cost, description=desc_cost, example=ex_cost, ge=1)
    show_price: Optional[bool] = Field(title=title_show_price, description=desc_show_price, example=ex_show_price)
    service_type_id: UUID4 = Field(title=title_service_type_id, description=desc_service_type_id, example=ex_service_type_id)

    class Config:
        orm_mode = True


class PriceListResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    key: str = Field(title=title_key, description=desc_key, max_length=255, min_length=3, example=ex_key)
    hierarchy: int = Field(title=title_hierarchy, description=desc_hierarchy, example=ex_hierarchy, ge=1)
    cost: float = Field(title=title_cost, description=desc_cost, example=ex_cost, ge=1)
    show_price: bool = Field(title=title_show_price, description=desc_show_price, example=ex_show_price)
    service_type_id: ServiceTypeResponse
    job_center_id: JobCenterResponse

    class Config:
        orm_mode = True
