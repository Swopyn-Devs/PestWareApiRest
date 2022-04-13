from typing import Optional
from pydantic import Field
from documentation.job_centers import *

from pydantic import BaseModel, UUID4, EmailStr


class JobCenterRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    business_name: str = Field(title=title_business_name, description=desc_business_name, max_length=255, min_length=3,
                               example=ex_business_name)
    health_manager: Optional[str] = Field(title=title_health_manager, description=desc_health_manager, max_length=255,
                                          min_length=3, example=ex_health_manager)
    company_id: UUID4 = Field(title=title_company_id, description=desc_company_id, example=ex_company_id)
    taxpayer_registration: Optional[str] = Field(title=title_taxpayer_registration,
                                                 description=desc_taxpayer_registration,
                                                 example=ex_taxpayer_registration)
    license_number: Optional[str] = Field(title=title_license_number, description=desc_license_number,
                                          example=ex_license_number)
    email: Optional[EmailStr] = Field(title=title_email, description=desc_email, example=ex_email)
    phone: Optional[str] = Field(title=title_phone, description=desc_phone, example=ex_phone)
    whatsapp: Optional[str] = Field(title=title_whatsapp, description=desc_whatsapp, example=ex_whatsapp)
    web_page: Optional[str] = Field(title=title_web_page, description=desc_web_page, example=ex_web_page)
    facebook: Optional[str] = Field(title=title_facebook, description=desc_facebook, example=ex_facebook)
    messenger: Optional[str] = Field(title=title_messenger, description=desc_messenger, example=ex_messenger)
    timezone: Optional[str] = Field(title=title_timezone, description=desc_timezone, example=ex_timezone)

    class Config:
        orm_mode = True


class JobCenterResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    business_name: str = Field(title=title_business_name, description=desc_business_name, max_length=255, min_length=3,
                               example=ex_business_name)
    health_manager: Optional[str] = Field(title=title_health_manager, description=desc_health_manager, max_length=255,
                                          min_length=3, example=ex_health_manager)
    company_id: UUID4 = Field(title=title_company_id, description=desc_company_id, example=ex_timezone)
    taxpayer_registration: Optional[str] = Field(title=title_taxpayer_registration,
                                                 description=desc_taxpayer_registration,
                                                 example=ex_taxpayer_registration)
    license_number: Optional[str] = Field(title=title_license_number, description=desc_license_number,
                                          example=ex_license_number)
    email: Optional[EmailStr] = Field(title=title_email, description=desc_email, example=ex_email)
    phone: Optional[str] = Field(title=title_phone, description=desc_phone, example=ex_phone)
    whatsapp: Optional[str] = Field(title=title_whatsapp, description=desc_whatsapp, example=ex_whatsapp)
    web_page: Optional[str] = Field(title=title_web_page, description=desc_web_page, example=ex_web_page)
    facebook: Optional[str] = Field(title=title_facebook, description=desc_facebook, example=ex_facebook)
    messenger: Optional[str] = Field(title=title_messenger, description=desc_messenger, example=ex_messenger)
    timezone: Optional[str] = Field(title=title_timezone, description=desc_timezone, example=ex_timezone)
    sanitary_license: Optional[str] = Field(title=title_sanitary_license, description=desc_sanitary_license,
                                            example=ex_sanitary_license)

    class Config:
        orm_mode = True
