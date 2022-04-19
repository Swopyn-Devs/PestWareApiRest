from pydantic import BaseModel, UUID4, Field
from documentation.discounts import *


class DiscountRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    description: str = Field(title=title_description, description=desc_description, max_length=255, min_length=3, example=ex_description)
    percentage: int = Field(title=title_percentage, description=desc_percentage, example=ex_percentage, ge=1, le=100)

    class Config:
        orm_mode = True


class DiscountUpdateRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    description: str = Field(title=title_description, description=desc_description, max_length=255, min_length=3, example=ex_description)
    percentage: int = Field(title=title_percentage, description=desc_percentage, example=ex_percentage, ge=1, le=100)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True


class DiscountResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    description: str = Field(title=title_description, description=desc_description, max_length=255, min_length=3, example=ex_description)
    percentage: int = Field(title=title_percentage, description=desc_percentage, example=ex_percentage, ge=1, le=100)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True
