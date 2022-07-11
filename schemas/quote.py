from datetime import datetime
from pydantic import BaseModel, UUID4, Field
from typing import Optional
from documentation.quotes import *
from schemas.job_center import JobCenterResponse
from schemas.employee import EmployeeResponse
from schemas.origin_source import OriginSourceResponse
from schemas.discount import DiscountResponse
from schemas.customer import CustomerResponse
from schemas.service_type import ServiceTypeResponse
from schemas.price_list import PriceListResponse
from schemas.status import StatusResponse
from schemas.rejection_reason import RejectionReasonResponse


class QuoteRequest(BaseModel):
    quantity: Optional[int] = Field(title=title_quantity, description=desc_quantity, example=ex_quantity)
    subtotal: float = Field(title=title_subtotal, description=desc_subtotal, example=ex_subtotal)
    total: float = Field(title=title_total, description=desc_total, example=ex_total)
    tax: float = Field(title=title_tax, description=desc_tax, example=ex_tax)
    sent_mail: bool = Field(title=title_sent_mail, description=desc_sent_mail, example=ex_sent_mail)
    sent_whatsapp: bool = Field(title=title_sent_whatsapp, description=desc_sent_whatsapp, example=ex_sent_whatsapp)
    approved: bool = Field(title=title_approved, description=desc_approved, example=ex_approved)
    service_type_id: UUID4 = Field(title=title_service_type_id, description=desc_service_type_id, example=ex_service_type_id)
    customer_id: UUID4 = Field(title=title_customer_id, description=desc_customer_id, example=ex_customer_id)
    origin_source_id: Optional[UUID4] = None
    discount_id: Optional[UUID4] = None
    employee_id: UUID4 = Field(title=title_employee_id, description=desc_employee_id, example=ex_employee_id)
    price_list_id: Optional[UUID4] = None

    class Config:
        orm_mode = True


class QuoteUpdateRequest(BaseModel):
    quantity: Optional[int] = Field(title=title_quantity, description=desc_quantity, example=ex_quantity)
    subtotal: float = Field(title=title_subtotal, description=desc_subtotal, example=ex_subtotal)
    total: float = Field(title=title_total, description=desc_total, example=ex_total)
    tax: float = Field(title=title_tax, description=desc_tax, example=ex_tax)
    sent_mail: bool = Field(title=title_sent_mail, description=desc_sent_mail, example=ex_sent_mail)
    sent_whatsapp: bool = Field(title=title_sent_whatsapp, description=desc_sent_whatsapp, example=ex_sent_whatsapp)
    approved: bool = Field(title=title_approved, description=desc_approved, example=ex_approved)
    service_type_id: UUID4 = Field(title=title_service_type_id, description=desc_service_type_id, example=ex_service_type_id)
    customer_id: UUID4 = Field(title=title_customer_id, description=desc_customer_id, example=ex_customer_id)
    origin_source_id: Optional[UUID4] = None
    discount_id: Optional[UUID4] = None
    employee_id: UUID4 = Field(title=title_employee_id, description=desc_employee_id, example=ex_employee_id)
    price_list_id: Optional[UUID4] = None
    job_center_id: UUID4 = Field(title=title_job_center_id, description=desc_job_center_id, example=ex_job_center_id)

    class Config:
        orm_mode = True


class QuoteApproveRequest(BaseModel):
    approved: bool = Field(title=title_approved, description=desc_approved, example=ex_approved)

    class Config:
        orm_mode = True


class QuoteRejectRequest(BaseModel):
    rejection_reason_id: UUID4 = Field(title=title_rejection_reason_id, description=desc_rejection_reason_id, example=ex_rejection_reason_id)
    rejection_reason_comment: str = Field(title=title_rejection_reason_comment, description=desc_rejection_reason_comment, example=ex_rejection_reason_comment)

    class Config:
        orm_mode = True


class QuoteResponse(BaseModel):
    id: UUID4
    folio: str = Field(title=title_folio, description=desc_total, example=ex_total)
    quantity: Optional[int] = Field(title=title_quantity, description=desc_quantity, example=ex_quantity)
    total: float = Field(title=title_total, description=desc_total, example=ex_total)
    tax: float = Field(title=title_tax, description=desc_tax, example=ex_tax)
    sent_mail: bool = Field(title=title_sent_mail, description=desc_sent_mail, example=ex_sent_mail)
    sent_whatsapp: bool = Field(title=title_sent_whatsapp, description=desc_sent_whatsapp, example=ex_sent_whatsapp)
    approved: bool = Field(title=title_approved, description=desc_approved, example=ex_approved)
    service_type_id: ServiceTypeResponse
    customer_id: CustomerResponse
    origin_source_id: Optional[OriginSourceResponse] = None
    discount_id: Optional[DiscountResponse] = None
    employee_id: EmployeeResponse
    price_list_id: Optional[PriceListResponse] = None
    status_id: StatusResponse
    job_center_id: JobCenterResponse
    rejection_reason_id: Optional[RejectionReasonResponse] = None
    rejection_reason_comment: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
