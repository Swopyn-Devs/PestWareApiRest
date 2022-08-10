from typing import Optional, Union
from pydantic import BaseModel, UUID4, Field
from documentation.mip_inspection_form import *
from schemas.event import EventResponse, EventBasicResponse


class MIPInspectionFormRequest(BaseModel):
    event_id: UUID4 = Field(title=title_event_id, description=desc_event_id, example=ex_event_id)
    nesting_areas: Optional[str] = Field(title=title_nesting_areas, description=desc_nesting_areas, example=ex_nesting_areas)
    comments: Optional[str] = Field(title=title_comments, description=desc_comments, example=ex_comments)

    class Config:
        orm_mode = True


class MIPInspectionFormResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    event_id: Union[EventResponse, EventBasicResponse]
    nesting_areas: Optional[str] = Field(title=title_nesting_areas, description=desc_nesting_areas, example=ex_nesting_areas)
    comments: Optional[str] = Field(title=title_comments, description=desc_comments, example=ex_comments)

    class Config:
        orm_mode = True


class MIPInspectionFormBasicResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    event_id: UUID4
    nesting_areas: Optional[str] = Field(title=title_nesting_areas, description=desc_nesting_areas, example=ex_nesting_areas)
    comments: Optional[str] = Field(title=title_comments, description=desc_comments, example=ex_comments)

    class Config:
        orm_mode = True
