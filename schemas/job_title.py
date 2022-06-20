from typing import Optional
from pydantic import BaseModel, UUID4
from schemas.job_center import JobCenterResponse


class JobTitleRequest(BaseModel):
    name: str

    class Config:
        orm_mode = True


class JobTitleUpdateRequest(BaseModel):
    name: str
    job_center_id: UUID4

    class Config:
        orm_mode = True


class JobTitleResponse(BaseModel):
    id: UUID4
    name: str
    job_center_id: JobCenterResponse

    class Config:
        orm_mode = True
