from typing import Optional
from datetime import datetime

from pydantic import BaseModel, UUID4, Field

from documentation.company import *


class CompanyRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    contact_name: str = Field(title=title_c_name, description=desc_c_name, max_length=255, example=ex_c_name)
    contact_email: str = Field(title=title_c_email, description=desc_c_email, max_length=255, example=ex_c_email)
    contact_phone: str = Field(title=title_c_phone, description=desc_c_phone, example=ex_c_phone)
    country_id: UUID4 = Field(title=title_country, description=desc_country, example=ex_country)
    web_color: Optional[str] = Field(title=title_color, description=desc_color, example=ex_color)

    class Config:
        orm_mode = True


class CompanyResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    folio: str = Field(title=title_folio, description=desc_folio, example=ex_folio)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    slug: str = Field(title=title_slug, description=desc_slug, example=ex_slug)
    contact_name: str = Field(title=title_c_name, description=desc_c_name, max_length=255, example=ex_c_name)
    contact_email: str = Field(title=title_c_email, description=desc_c_email, max_length=255, example=ex_c_email)
    contact_phone: str = Field(title=title_c_phone, description=desc_c_phone, example=ex_c_phone)
    country_id: UUID4 = Field(title=title_country, description=desc_country, example=ex_country)
    document_logo: Optional[str] = Field(title=title_logo_d, description=desc_logo_d, example=ex_logo_d)
    document_stamp: Optional[str] = Field(title=title_stamp_d, description=desc_stamp_d, example=ex_stamp_d)
    web_logo: Optional[str] = Field(title=title_logo_w, description=desc_logo_w, example=ex_logo_w)
    web_color: Optional[str] = Field(title=title_color, description=desc_color, example=ex_color)
    cutoff_date: Optional[str] = Field(title=title_cutoff, description=desc_cutoff, example=ex_cutoff)
    is_active: bool = Field(title=title_active, description=desc_active)
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class CompanyColorRequest(BaseModel):
    web_color: Optional[str] = Field(title=title_color, description=desc_color, example=ex_color)
