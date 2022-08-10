from typing import Union, Optional
from pydantic import BaseModel, UUID4
from datetime import date as dateF, datetime, time as timeF
from schemas.event_type import EventTypeResponse, EventTypeBasicResponse
from schemas.quote import QuoteResponse, QuoteBasicResponse
from schemas.customer import CustomerResponse, CustomerBasicResponse
from schemas.employee import EmployeeResponse, EmployeeBasicResponse
from schemas.service_type import ServiceTypeResponse, ServiceTypeBasicResponse
from schemas.job_center import JobCenterResponse, JobCenterBasicResponse
from schemas.status import StatusResponse


class EventRequest(BaseModel):
    title: str
    event_type_id: UUID4
    initial_date: dateF
    final_date: dateF
    initial_hour: timeF
    final_hour: timeF
    quote_id: Optional[UUID4]
    customer_id: Optional[UUID4]
    employee_id: Optional[UUID4]
    service_type_id: Optional[UUID4]
    total: Optional[float]
    comments: Optional[str]

    class Config:
        orm_mode = True


class EventUpdateRequest(BaseModel):
    title: str
    event_type_id: UUID4
    initial_date: dateF
    final_date: dateF
    initial_hour: timeF
    final_hour: timeF
    quote_id: Optional[UUID4]
    customer_id: Optional[UUID4]
    employee_id: Optional[UUID4]
    service_type_id: Optional[UUID4]
    total: Optional[float]
    comments: Optional[str]
    job_center_id: UUID4

    class Config:
        orm_mode = True
        
        
class EventResponse(BaseModel):
    id: UUID4
    title: str
    folio: str
    event_type_id: Union[EventTypeResponse, EventTypeBasicResponse]
    initial_date: dateF
    final_date: dateF
    initial_hour: timeF
    final_hour: timeF
    real_initial_date: Optional[Union[dateF, str]] = None
    real_final_date: Optional[Union[dateF, str]] = None
    real_initial_hour: Optional[Union[timeF, str]] = None
    real_final_hour: Optional[Union[timeF, str]] = None
    start_latitude: Optional[Union[float, str]] = None
    start_longitude: Optional[Union[float, str]] = None
    end_latitude: Optional[Union[float, str]] = None
    end_longitude: Optional[Union[float, str]] = None
    quote_id: Optional[Union[QuoteResponse, QuoteBasicResponse]] = None
    customer_id: Optional[Union[CustomerResponse, CustomerBasicResponse]] = None
    employee_id: Optional[Union[EmployeeResponse, EmployeeBasicResponse]] = None
    service_type_id: Optional[Union[ServiceTypeResponse, ServiceTypeBasicResponse]] = None
    subtotal: Optional[float]
    discount: Optional[float]
    extra: Optional[float]
    tax: Optional[float]
    total: Optional[float]
    comments: Optional[str]
    mip_inspection_form_id: Optional[UUID4] = None
    mip_condition_form_id: Optional[UUID4] = None
    mip_control_form_id: Optional[UUID4] = None
    mip_payment_form_id: Optional[UUID4] = None
    mip_signature_form_id: Optional[UUID4] = None
    status_id: StatusResponse = None
    job_center_id: Union[JobCenterResponse, JobCenterBasicResponse]
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class EventBasicResponse(BaseModel):
    id: UUID4
    title: str
    folio: str
    event_type_id: UUID4
    initial_date: dateF
    final_date: dateF
    initial_hour: timeF
    final_hour: timeF
    real_initial_date: Optional[Union[dateF, str]] = None
    real_final_date: Optional[Union[dateF, str]] = None
    real_initial_hour: Optional[Union[timeF, str]] = None
    real_final_hour: Optional[Union[timeF, str]] = None
    start_latitude: Optional[Union[float, str]] = None
    start_longitude: Optional[Union[float, str]] = None
    end_latitude: Optional[Union[float, str]] = None
    end_longitude: Optional[Union[float, str]] = None
    quote_id: Optional[UUID4] = None
    customer_id: Optional[UUID4] = None
    employee_id: Optional[UUID4] = None
    service_type_id: Optional[UUID4] = None
    subtotal: Optional[float]
    discount: Optional[float]
    extra: Optional[float]
    tax: Optional[float]
    total: Optional[float]
    comments: Optional[str]
    mip_inspection_form_id: Optional[UUID4] = None
    mip_condition_form_id: Optional[UUID4] = None
    mip_control_form_id: Optional[UUID4] = None
    mip_payment_form_id: Optional[UUID4] = None
    mip_signature_form_id: Optional[UUID4] = None
    status_id: UUID4 = None
    job_center_id: UUID4
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
