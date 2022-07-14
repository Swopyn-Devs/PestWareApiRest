from typing import Optional, Union
from pydantic import BaseModel, UUID4, Field
from documentation.quote_extras import *
from schemas.quote import QuoteResponse, QuoteBasicResponse
from schemas.extra import ExtraResponse, ExtraBasicResponse


class QuoteExtraRequest(BaseModel):
    extra_id: UUID4 = Field(title=title_extra_id, description=desc_extra_id, example=ex_extra_id)
    quantity: Optional[int] = Field(title=title_quantity, description=desc_quantity, example=ex_quantity)

    class Config:
        orm_mode = True


class QuoteExtraResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    quote_id: Union[QuoteResponse, QuoteBasicResponse]
    extra_id: Union[ExtraResponse, ExtraBasicResponse]
    quantity: Optional[int] = Field(title=title_quantity, description=desc_quantity, example=ex_quantity)

    class Config:
        orm_mode = True
