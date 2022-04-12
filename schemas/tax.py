from pydantic import BaseModel, UUID4, Field
from documentation.taxes import *


class TaxRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    value: int = Field(title=title_value, description=desc_value, example=ex_value)

    class Config:
        orm_mode = True


class TaxUpdateRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    value: int = Field(title=title_value, description=desc_value, example=ex_value)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True


class TaxResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    value: int = Field(title=title_value, description=desc_value, example=ex_value)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True
