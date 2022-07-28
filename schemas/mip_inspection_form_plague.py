from typing import Optional, Union
from pydantic import BaseModel, UUID4, Field
from documentation.mip_inspection_form_plagues import *
from schemas.mip_inspection_form import MIPInspectionFormResponse, MIPInspectionFormBasicResponse
from schemas.plague import PlagueResponse, PlagueBasicResponse
from schemas.infestation_degree import InfestationDegreeResponse, InfestationDegreeBasicResponse
from schemas.nesting_area import NestingAreaResponse, NestingAreaBasicResponse


class MIPInspectionFormPlagueRequest(BaseModel):
    plague_id: UUID4 = Field(title=title_plague_id, description=desc_plague_id, example=ex_plague_id)
    infestation_degree_id: UUID4 = Field(title=title_infestation_degree_id, description=desc_infestation_degree_id, example=ex_infestation_degree_id)
    nesting_area_id: Optional[UUID4] = Field(title=title_nesting_area_id, description=desc_nesting_area_id, example=ex_nesting_area_id)
    comments: Optional[str] = Field(title=title_comments, description=desc_comments, example=ex_comments)

    class Config:
        orm_mode = True


class MIPInspectionFormPlagueResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    mip_inspection_form_id: Union[MIPInspectionFormResponse, MIPInspectionFormBasicResponse]
    plague_id: Union[PlagueResponse, PlagueBasicResponse]
    infestation_degree_id: Union[InfestationDegreeResponse, InfestationDegreeBasicResponse]
    nesting_area_id: Optional[Union[NestingAreaResponse, NestingAreaBasicResponse]] = None
    comments: Optional[str] = Field(title=title_comments, description=desc_comments, example=ex_comments)

    class Config:
        orm_mode = True


class MIPInspectionFormPlagueBasicResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    mip_inspection_form_id: UUID4
    plague_id: UUID4
    infestation_degree_id: UUID4
    nesting_area_id: Optional[UUID4] = None
    comments: Optional[str] = Field(title=title_comments, description=desc_comments, example=ex_comments)

    class Config:
        orm_mode = True
