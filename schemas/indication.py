from pydantic import BaseModel, UUID4, Field
from documentation.indications import *


class IndicationRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    key: str = Field(title=title_key, description=desc_key, max_length=20, min_length=2, example=ex_key)
    description: str = Field(title=title_description, description=desc_description, max_length=500, min_length=3, example=ex_description)

    class Config:
        orm_mode = True


class IndicationUpdateRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    key: str = Field(title=title_key, description=desc_key, max_length=20, min_length=2, example=ex_key)
    description: str = Field(title=title_description, description=desc_description, max_length=500, min_length=3, example=ex_description)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True


class IndicationResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    key: str = Field(title=title_key, description=desc_key, max_length=20, min_length=2, example=ex_key)
    description: str = Field(title=title_description, description=desc_description, max_length=500, min_length=3, example=ex_description)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True
