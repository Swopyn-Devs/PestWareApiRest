from pydantic import BaseModel, UUID4, Field
from datetime import date as dateF, time as timeF
from documentation.quote_tracing import *
from schemas.quote import QuoteResponse


class QuoteTracingRequest(BaseModel):
    date: dateF = Field(title=title_date, description=desc_date, example=ex_date)
    time: timeF = Field(title=title_time, description=desc_time, example=ex_time)
    comment: str = Field(title=title_comment, description=desc_comment, example=ex_comment)

    class Config:
        orm_mode = True


class QuoteTracingResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    quote_id: QuoteResponse
    date: dateF = Field(title=title_date, description=desc_date, example=ex_date)
    time: timeF = Field(title=title_time, description=desc_time, example=ex_time)
    comment: str = Field(title=title_comment, description=desc_comment, example=ex_comment)

    class Config:
        orm_mode = True
