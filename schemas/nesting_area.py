from typing import Union
from pydantic import BaseModel, UUID4, Field
from documentation.nesting_areas import *
from schemas.customer import CustomerResponse, CustomerBasicResponse


class NestingAreaRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    customer_id: UUID4 = Field(title=title_customer_id, description=desc_customer_id, example=ex_customer_id)

    class Config:
        orm_mode = True


class NestingAreaResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    customer_id: Union[CustomerResponse, CustomerBasicResponse]

    class Config:
        orm_mode = True


class NestingAreaBasicResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    customer_id: UUID4

    class Config:
        orm_mode = True
