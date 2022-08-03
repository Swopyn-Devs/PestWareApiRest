from typing import Optional, Union
from pydantic import BaseModel, UUID4, Field
from documentation.mip_payment_form_photos import *
from schemas.mip_payment_form import MIPPaymentFormResponse, MIPPaymentFormBasicResponse


class MIPPaymentFormPhotoRequest(BaseModel):
    comments: Optional[str] = Field(title=title_comments, description=desc_comments, example=ex_comments)

    class Config:
        orm_mode = True


class MIPPaymentFormPhotoResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    mip_payment_form_id: Union[MIPPaymentFormResponse, MIPPaymentFormBasicResponse]
    photo: str = Field(title=title_photo, description=desc_photo, example=ex_photo)
    comments: Optional[str] = Field(title=title_comments, description=desc_comments, example=ex_comments)

    class Config:
        orm_mode = True


class MIPPaymentFormPhotoBasicResponse(BaseModel):
    id: UUID4 = Field(title=title_id, description=desc_id, example=ex_id)
    mip_payment_form_id: UUID4
    photo: str = Field(title=title_photo, description=desc_photo, example=ex_photo)
    comments: Optional[str] = Field(title=title_comments, description=desc_comments, example=ex_comments)

    class Config:
        orm_mode = True
