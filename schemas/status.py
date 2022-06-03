from pydantic import BaseModel, UUID4, Field
from documentation.status import *


class StatusRequest(BaseModel):
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    key_string: str = Field(title=title_key_string, description=desc_key_string, max_length=255, min_length=3, example=ex_key_string)
    module: str = Field(title=title_module, description=desc_module, max_length=255, min_length=3, example=ex_module)

    class Config:
        orm_mode = True


class StatusResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    name: str = Field(title=title_name, description=desc_name, max_length=255, min_length=3, example=ex_name)
    key_string: str = Field(title=title_key_string, description=desc_key_string, max_length=255, min_length=3, example=ex_key_string)
    module: str = Field(title=title_module, description=desc_module, max_length=255, min_length=3, example=ex_module)

    class Config:
        orm_mode = True
