from pydantic import BaseModel, UUID4, Field
from documentation.quote_plagues import *
from schemas.quote import QuoteResponse
from schemas.plague import PlagueResponse


class QuotePlagueRequest(BaseModel):
    plague_id: UUID4 = Field(title=title_plague_id, description=desc_plague_id, example=ex_plague_id)

    class Config:
        orm_mode = True


class QuotePlagueResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    quote_id: QuoteResponse
    plague_id: PlagueResponse

    class Config:
        orm_mode = True
