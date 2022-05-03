from pydantic import BaseModel, UUID4, Field
from documentation.price_list_prices import *


class PriceListPriceRequest(BaseModel):
    scale: int = Field(title=title_scale, description=desc_scale, example=ex_scale, ge=1)
    price_one: float = Field(title=title_price_one, description=desc_price_one, example=ex_price_one, ge=0)
    price_two: float = Field(title=title_price_two, description=desc_price_two, example=ex_price_two, ge=0)

    class Config:
        orm_mode = True


class PriceListPriceResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    price_list_id: UUID4 = Field(title=title_price_list_id, description=desc_price_list_id, example=ex_price_list_id)
    scale: int = Field(title=title_scale, description=desc_scale, example=ex_scale, ge=1)
    price_one: float = Field(title=title_price_one, description=desc_price_one, example=ex_price_one, ge=0)
    price_two: float = Field(title=title_price_two, description=desc_price_two, example=ex_price_two, ge=0)

    class Config:
        orm_mode = True
