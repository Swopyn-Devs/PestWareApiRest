from typing import Optional

from pydantic import BaseModel, UUID4


class CompanyRequest(BaseModel):
    name: str
    contact_name: str
    contact_email: str
    contact_phone: str
    country_id: UUID4
    web_color: Optional[str] = None

    class Config:
        orm_mode = True


class CompanyResponse(BaseModel):
    id: UUID4
    folio: str
    name: str
    slug: str
    contact_name: str
    contact_email: str
    contact_phone: str
    country_id: UUID4
    document_logo: Optional[str] = None
    document_stamp: Optional[str] = None
    web_logo: Optional[str] = None
    web_color: Optional[str] = None
    cutoff_date: Optional[str] = None
    is_active: bool

    class Config:
        orm_mode = True
