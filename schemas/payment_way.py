from pydantic import BaseModel, UUID4, Field
from documentation.payment_ways import *
from schemas.job_center import JobCenterResponse


class PaymentWayRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    credit_days: int = Field(title=title_credit_days, description=desc_credit_days, example=ex_credit_days)

    class Config:
        orm_mode = True


class PaymentWayUpdateRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    credit_days: int = Field(title=title_credit_days, description=desc_credit_days, example=ex_credit_days)
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True


class PaymentWayResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    credit_days: int = Field(title=title_credit_days, description=desc_credit_days, example=ex_credit_days)
    job_center_id: JobCenterResponse

    class Config:
        orm_mode = True
