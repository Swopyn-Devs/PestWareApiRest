from typing import Optional, Union
from pydantic import BaseModel, UUID4, Field
from documentation.mip_condition_form import *
from schemas.event import EventResponse, EventBasicResponse


class MIPConditionFormRequest(BaseModel):
    event_id: UUID4 = Field(title=title_event_id, description=desc_event_id, example=ex_event_id)
    indications: bool = Field(title=title_indications, description=desc_indications, example=ex_indications)
    restricted_access: Optional[str] = Field(title=title_restricted_access, description=desc_restricted_access, example=ex_restricted_access)
    comments: Optional[str] = Field(title=title_comments, description=desc_comments, example=ex_comments)

    class Config:
        orm_mode = True


class MIPConditionFormResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    event_id: Union[EventResponse, EventBasicResponse]
    indications: bool = Field(title=title_indications, description=desc_indications, example=ex_indications)
    restricted_access: Optional[str] = Field(title=title_restricted_access, description=desc_restricted_access, example=ex_restricted_access)
    comments: Optional[str] = Field(title=title_comments, description=desc_comments, example=ex_comments)

    class Config:
        orm_mode = True


class MIPConditionFormBasicResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    event_id: UUID4
    indications: Optional[str] = Field(title=title_indications, description=desc_indications, example=ex_indications)
    restricted_access: Optional[str] = Field(title=title_restricted_access, description=desc_restricted_access, example=ex_restricted_access)
    comments: Optional[str] = Field(title=title_comments, description=desc_comments, example=ex_comments)

    class Config:
        orm_mode = True
