from typing import Union
from pydantic import BaseModel, UUID4
from schemas.job_center import JobCenterResponse, JobCenterBasicResponse


class EventTypeRequest(BaseModel):
    name: str
    quote_field: bool
    customer_field: bool
    employee_field: bool
    service_type_field: bool
    plagues_field: bool
    cost_field: bool
    comments_field: bool
    inspection_form: bool
    condition_form: bool
    control_form: bool
    payment_form: bool
    signature_form: bool
    notification_action: bool
    reminder_action: bool
    folio_key_setting: str
    folio_init_setting: int
    is_service_order: bool
    
    class Config:
        orm_mode = True
        
        
class EventTypeUpdateRequest(BaseModel):
    name: str
    quote_field: bool
    customer_field: bool
    employee_field: bool
    service_type_field: bool
    plagues_field: bool
    cost_field: bool
    comments_field: bool
    inspection_form: bool
    condition_form: bool
    control_form: bool
    payment_form: bool
    signature_form: bool
    notification_action: bool
    reminder_action: bool
    folio_key_setting: str
    folio_init_setting: int
    is_service_order: bool
    job_center_id: UUID4
    
    class Config:
        orm_mode = True
        
        
class EventTypeResponse(BaseModel):
    id: UUID4
    name: str
    quote_field: bool
    customer_field: bool
    employee_field: bool
    service_type_field: bool
    plagues_field: bool
    cost_field: bool
    comments_field: bool
    inspection_form: bool
    condition_form: bool
    control_form: bool
    payment_form: bool
    signature_form: bool
    notification_action: bool
    reminder_action: bool
    folio_key_setting: str
    folio_init_setting: int
    is_service_order: bool
    job_center_id: Union[JobCenterResponse, JobCenterBasicResponse]
    
    class Config:
        orm_mode = True
        
        
class EventTypeBasicResponse(BaseModel):
    id: UUID4
    name: str
    quote_field: bool
    customer_field: bool
    employee_field: bool
    service_type_field: bool
    plagues_field: bool
    cost_field: bool
    comments_field: bool
    inspection_form: bool
    condition_form: bool
    control_form: bool
    payment_form: bool
    signature_form: bool
    notification_action: bool
    reminder_action: bool
    folio_key_setting: str
    folio_init_setting: int
    is_service_order: bool
    job_center_id: UUID4
    
    class Config:
        orm_mode = True
