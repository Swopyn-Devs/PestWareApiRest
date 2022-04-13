from pydantic import BaseModel, UUID4, Field
from documentation.concepts import *


class ConceptRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    type: str = Field(title=title_type, description=desc_type, max_length=255, min_length=3, example=ex_type)

    class Config:
        orm_mode = True


class ConceptUpdateRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    type: str = Field(title=title_type, description=desc_type, max_length=255, min_length=3, example=ex_type)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True


class ConceptResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    type: str = Field(title=title_type, description=desc_type, max_length=255, min_length=3, example=ex_type)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True
