from typing import Union
from pydantic import BaseModel, UUID4, Field
from documentation.mip_condition_form_cleaning import *
from schemas.mip_condition_form import MIPConditionFormResponse, MIPConditionFormBasicResponse
from schemas.cleaning import CleaningResponse, CleaningBasicResponse


class MIPConditionFormCleaningRequest(BaseModel):
    cleaning_id: UUID4 = Field(title=title_cleaning_id, description=desc_cleaning_id, example=ex_cleaning_id)

    class Config:
        orm_mode = True


class MIPConditionFormCleaningResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    mip_condition_form_id: Union[MIPConditionFormResponse, MIPConditionFormBasicResponse]
    cleaning_id: Union[CleaningResponse, CleaningBasicResponse]

    class Config:
        orm_mode = True


class MIPConditionFormCleaningBasicResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    mip_condition_form_id: UUID4
    cleaning_id: UUID4

    class Config:
        orm_mode = True
