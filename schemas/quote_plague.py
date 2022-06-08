from pydantic import BaseModel, UUID4, Field
from documentation.quote_plagues import *


class QuotePlagueRequest(BaseModel):
    plague_id: UUID4 = Field(title=title_plague_id, description=desc_plague_id, example=ex_plague_id)

    class Config:
        orm_mode = True


class QuotePlagueResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    quote_id: UUID4 = Field(title=title_quote_id, description=desc_quote_id, example=ex_quote_id)
    plague_id: UUID4 = Field(title=title_plague_id, description=desc_plague_id, example=ex_plague_id)

    class Config:
        orm_mode = True
