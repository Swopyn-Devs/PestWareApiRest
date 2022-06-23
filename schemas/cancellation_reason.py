from pydantic import BaseModel, UUID4, Field
from documentation.cancellation_reasons import *
from schemas.job_center import JobCenterResponse


class CancellationReasonRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)

    class Config:
        orm_mode = True


class CancellationReasonUpdateRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True


class CancellationReasonResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    job_center_id: JobCenterResponse

    class Config:
        orm_mode = True
