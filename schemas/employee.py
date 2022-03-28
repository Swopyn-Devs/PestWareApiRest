from typing import Optional

from pydantic import BaseModel, UUID4


class EmployeeRequest(BaseModel):
    name: str
    company_id: UUID4
    job_center_id: UUID4
    job_title_id: UUID4
    color: Optional[str] = None

    class Config:
        orm_mode = True


class EmployeeResponse(BaseModel):
    id: UUID4
    name: str
    company_id: UUID4
    job_center_id: UUID4
    job_title_id: UUID4
    avatar: Optional[str] = None
    signature: Optional[str] = None
    color: Optional[str] = None

    class Config:
        orm_mode = True
