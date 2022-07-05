from typing import Optional
from pydantic import BaseModel, UUID4, Field
from documentation.quote_concepts import *
from schemas.quote import QuoteResponse


class QuoteConceptRequest(BaseModel):
    concept: str = Field(title=title_concept, description=desc_concept, example=ex_concept)
    quantity: Optional[int] = Field(title=title_quantity, description=desc_quantity, example=ex_quantity)
    unit_price: Optional[float] = Field(title=title_unit_price, description=desc_unit_price, example=ex_unit_price)
    tax: Optional[float] = Field(title=title_tax, description=desc_tax, example=ex_tax)
    subtotal: Optional[float] = Field(title=title_subtotal, description=desc_subtotal, example=ex_subtotal)
    total: Optional[float] = Field(title=title_total, description=desc_total, example=ex_total)

    class Config:
        orm_mode = True


class QuoteConceptResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    quote_id: QuoteResponse
    concept: str = Field(title=title_concept, description=desc_concept, example=ex_concept)
    quantity: Optional[int] = Field(title=title_quantity, description=desc_quantity, example=ex_quantity)
    unit_price: Optional[float] = Field(title=title_unit_price, description=desc_unit_price, example=ex_unit_price)
    tax: Optional[float] = Field(title=title_tax, description=desc_tax, example=ex_tax)
    subtotal: Optional[float] = Field(title=title_subtotal, description=desc_subtotal, example=ex_subtotal)
    total: Optional[float] = Field(title=title_total, description=desc_total, example=ex_total)

    class Config:
        orm_mode = True
