from pydantic import BaseModel, UUID4, Field
from documentation.price_list_plagues import *
from schemas.price_list import PriceListResponse
from schemas.plague import PlagueResponse


class PriceListPlagueRequest(BaseModel):
    plague_id: UUID4 = Field(title=title_plague_id, description=desc_plague_id, example=ex_plague_id)

    class Config:
        orm_mode = True


class PriceListPlagueResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    price_list_id: PriceListResponse
    plague_id: PlagueResponse

    class Config:
        orm_mode = True
