from typing import Union
from pydantic import BaseModel, UUID4, Field
from documentation.price_lists import *
from schemas.job_center import JobCenterResponse, JobCenterBasicResponse
from schemas.service_type import ServiceTypeResponse, ServiceTypeBasicResponse


class PriceListRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    key: str = Field(title=title_key, description=desc_key, max_length=255, min_length=3, example=ex_key)
    hierarchy: int = Field(title=title_hierarchy, description=desc_hierarchy, example=ex_hierarchy, ge=1)
    cost: float = Field(title=title_cost, description=desc_cost, example=ex_cost, ge=1)
    min_cost: float = Field(title=title_min_cost, description=desc_min_cost, example=ex_min_cost, ge=1)
    service_type_id: UUID4 = Field(title=title_service_type_id, description=desc_service_type_id, example=ex_service_type_id)

    class Config:
        orm_mode = True


class PriceListResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    key: str = Field(title=title_key, description=desc_key, max_length=255, min_length=3, example=ex_key)
    hierarchy: int = Field(title=title_hierarchy, description=desc_hierarchy, example=ex_hierarchy, ge=1)
    cost: float = Field(title=title_cost, description=desc_cost, example=ex_cost, ge=1)
    min_cost: float = Field(title=title_min_cost, description=desc_min_cost, example=ex_min_cost, ge=1)
    service_type_id: Union[ServiceTypeResponse, ServiceTypeBasicResponse]
    job_center_id: Union[JobCenterResponse, JobCenterBasicResponse]

    class Config:
        orm_mode = True


class PriceListBasicResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    key: str = Field(title=title_key, description=desc_key, max_length=255, min_length=3, example=ex_key)
    hierarchy: int = Field(title=title_hierarchy, description=desc_hierarchy, example=ex_hierarchy, ge=1)
    cost: float = Field(title=title_cost, description=desc_cost, example=ex_cost, ge=1)
    min_cost: float = Field(title=title_min_cost, description=desc_min_cost, example=ex_min_cost, ge=1)
    service_type_id: UUID4
    job_center_id: UUID4

    class Config:
        orm_mode = True
