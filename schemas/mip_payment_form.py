from typing import Optional, Union
from pydantic import BaseModel, UUID4, Field
from documentation.mip_payment_form import *
from schemas.event_type import EventTypeResponse, EventTypeBasicResponse
from schemas.payment_method import PaymentMethodResponse, PaymentMethodBasicResponse
from schemas.payment_way import PaymentWayResponse, PaymentWayBasicResponse
from schemas.status import StatusResponse


class MIPPaymentFormRequest(BaseModel):
    event_id: UUID4 = Field(title=title_event_id, description=desc_event_id, example=ex_event_id)
    payment_method_id: UUID4 = Field(title=title_payment_method_id, description=desc_payment_method_id, example=ex_payment_method_id)
    payment_way_id: UUID4 = Field(title=title_payment_way_id, description=desc_payment_way_id, example=ex_payment_way_id)
    amount: float = Field(title=title_amount, description=desc_amount, example=ex_amount)
    status_id: Optional[str] = Field(title=title_status_id, description=desc_status_id, example=ex_status_id)

    class Config:
        orm_mode = True


class MIPPaymentFormResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    event_id: Union[EventTypeResponse, EventTypeBasicResponse]
    payment_method_id: Union[PaymentMethodResponse, PaymentMethodBasicResponse]
    payment_way_id: Union[PaymentWayResponse, PaymentWayBasicResponse]
    amount: Optional[float] = Field(title=title_amount, description=desc_amount, example=ex_amount)
    status_id: Optional[StatusResponse]

    class Config:
        orm_mode = True


class MIPPaymentFormBasicResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    event_id: UUID4
    payment_method_id: UUID4
    payment_way_id: UUID4
    amount: Optional[float] = None
    status_id: Optional[UUID4] = None

    class Config:
        orm_mode = True
