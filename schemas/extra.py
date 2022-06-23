from pydantic import BaseModel, UUID4, Field
from documentation.extras import *
from schemas.job_center import JobCenterResponse


class ExtraRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    description: str = Field(title=title_description, description=desc_description, max_length=255, min_length=3, example=ex_description)
    quantity: int = Field(title=title_quantity, description=desc_quantity, example=ex_quantity)

    class Config:
        orm_mode = True


class ExtraUpdateRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    description: str = Field(title=title_description, description=desc_description, max_length=255, min_length=3, example=ex_description)
    quantity: int = Field(title=title_quantity, description=desc_quantity, example=ex_quantity)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True


class ExtraResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    description: str = Field(title=title_description, description=desc_description, max_length=255, min_length=3, example=ex_description)
    quantity: int = Field(title=title_quantity, description=desc_quantity, example=ex_quantity)
    job_center_id: JobCenterResponse

    class Config:
        orm_mode = True
