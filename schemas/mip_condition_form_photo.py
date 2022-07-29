from typing import Optional, Union
from pydantic import BaseModel, UUID4, Field
from documentation.mip_condition_form_photos import *
from schemas.mip_condition_form import MIPConditionFormResponse, MIPConditionFormBasicResponse


class MIPConditionFormPhotoRequest(BaseModel):
    comments: Optional[str] = Field(title=title_comments, description=desc_comments, example=ex_comments)

    class Config:
        orm_mode = True


class MIPConditionFormPhotoResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    mip_condition_form_id: Union[MIPConditionFormResponse, MIPConditionFormBasicResponse]
    photo: str = Field(title=title_photo, description=desc_photo, example=ex_photo)
    comments: Optional[str] = Field(title=title_comments, description=desc_comments, example=ex_comments)

    class Config:
        orm_mode = True


class MIPConditionFormPhotoBasicResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    mip_inspection_form_id: UUID4
    photo: str = Field(title=title_photo, description=desc_photo, example=ex_photo)
    comments: Optional[str] = Field(title=title_comments, description=desc_comments, example=ex_comments)

    class Config:
        orm_mode = True
