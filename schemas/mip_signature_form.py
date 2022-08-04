from typing import Union
from pydantic import BaseModel, UUID4, Field
from documentation.mip_signature_form import *
from schemas.event_type import EventTypeResponse, EventTypeBasicResponse


class MIPSignatureFormRequest(BaseModel):
    event_id: UUID4 = Field(title=title_event_id, description=desc_event_id, example=ex_event_id)
    name: str = Field(title=title_name, description=desc_name, example=ex_name)

    class Config:
        orm_mode = True


class MIPSignatureFormResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    event_id: Union[EventTypeResponse, EventTypeBasicResponse]
    signature: str = Field(title=title_signature, description=desc_signature, example=ex_signature)
    name: str = Field(title=title_name, description=desc_name, example=ex_name)

    class Config:
        orm_mode = True


class MIPSignatureFormBasicResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    event_id: UUID4
    signature: str = Field(title=title_signature, description=desc_signature, example=ex_signature)
    name: str = Field(title=title_name, description=desc_name, example=ex_name)

    class Config:
        orm_mode = True
