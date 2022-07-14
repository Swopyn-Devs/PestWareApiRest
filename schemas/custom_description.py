from typing import Union
from pydantic import BaseModel, UUID4, Field
from documentation.custom_descriptions import *
from schemas.job_center import JobCenterResponse, JobCenterBasicResponse


class CustomDescriptionRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    description: str = Field(title=title_description, description=desc_description, max_length=255, min_length=3, example=ex_description)

    class Config:
        orm_mode = True


class CustomDescriptionUpdateRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    description: str = Field(title=title_description, description=desc_description, max_length=255, min_length=3, example=ex_description)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True


class CustomDescriptionResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    description: str = Field(title=title_description, description=desc_description, max_length=255, min_length=3, example=ex_description)
    job_center_id: Union[JobCenterResponse, JobCenterBasicResponse]

    class Config:
        orm_mode = True
