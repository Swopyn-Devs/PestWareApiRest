from unicodedata import decimal, numeric

from numpy import double
from schemas.quote_extra import QuoteExtraRequest
from schemas.quote_concept import QuoteConceptRequest
from pydantic import BaseModel, UUID4
from typing import List, Optional


class QuoterRequest(BaseModel):
    service_type_id: UUID4
    quantity: float
    discount_id: Optional[UUID4]
    extras_quote: Optional[List[QuoteExtraRequest]]
    is_tax: bool
    
    
class QuoterConceptRequest(BaseModel):
    is_tax: bool
    discount_id: Optional[UUID4]
    extras_quote: Optional[List[QuoteExtraRequest]]
    concepts: List[QuoteConceptRequest]
    
    
class CalculateConceptRequest(BaseModel):
    concept: str
    quantity: Optional[int]
    unit_price: Optional[float]
    is_tax: bool


class QuoterResponse(BaseModel):
    price_list: Optional[UUID4]
    subtotal: float
    discount: float
    extras: float
    tax: float
    total: float

    class Config:
        orm_mode = True
        
        
class CalculateConceptResponse(BaseModel):
    subtotal: float
    tax: float
    total: float

    class Config:
        orm_mode = True
