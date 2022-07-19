from typing import Union
from pydantic import BaseModel, UUID4, Field
from documentation.plagues import *
from schemas.job_center import JobCenterResponse, JobCenterBasicResponse
from schemas.plague_category import PlagueCategoryResponse, PlagueCategoryBasicResponse


class PlagueRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    plague_category_id: str = Field(title=title_plague_category_id, description=desc_plague_category_id, example=ex_plague_category_id)

    class Config:
        orm_mode = True


class PlagueUpdateRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    plague_category_id: UUID4 = Field(title=title_plague_category_id, description=desc_plague_category_id, example=ex_plague_category_id)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True


class PlagueResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    plague_category_id: Union[PlagueCategoryResponse, PlagueCategoryBasicResponse]
    job_center_id: Union[JobCenterResponse, JobCenterBasicResponse]

    class Config:
        orm_mode = True


class PlagueBasicResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    plague_category_id: UUID4
    job_center_id: UUID4

    class Config:
        orm_mode = True
