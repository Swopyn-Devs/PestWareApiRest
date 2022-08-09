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
    real_initial_date: Optional[dateF]
    real_final_date: Optional[dateF]
    real_initial_hour: Optional[timeF]
    real_final_hour: Optional[timeF]
    start_latitude: Optional[float]
    start_longitude: Optional[float]
    end_latitude: Optional[float]
    end_longitude: Optional[float]
    quote_id: Optional[Union[QuoteResponse, QuoteBasicResponse]]
    customer_id: Optional[Union[CustomerResponse, CustomerBasicResponse]]
    employee_id: Optional[Union[EmployeeResponse, EmployeeBasicResponse]]
    service_type_id: Optional[Union[ServiceTypeResponse, ServiceTypeBasicResponse]]
    subtotal: Optional[float]
    discount: Optional[float]
    extra: Optional[float]
    tax: Optional[float]
    total: Optional[float]
    comments: Optional[str]
    mip_inspection_form_id: Optional[UUID4]
    mip_condition_form_id: Optional[UUID4]
    mip_control_form_id: Optional[UUID4]
    mip_payment_form_id: Optional[UUID4]
    mip_signature_form_id: Optional[UUID4]
    status_id: StatusResponse
    job_center_id: Union[JobCenterResponse, JobCenterBasicResponse]
    is_deleted: bool
    created_at: datetime
    updated_at: datetime