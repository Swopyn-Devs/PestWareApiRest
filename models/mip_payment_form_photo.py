from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class MIPPaymentFormPhoto(Base):
    __tablename__ = 'mip_payment_form_photo'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    mip_payment_form_id = Column(UUID(as_uuid=True), nullable=False)
    photo = Column(String, nullable=False)
    comments = Column(String, nullable=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class MIPPaymentFormPhotoAdmin(ModelAdmin, model=MIPPaymentFormPhoto):
    column_searchable_list = [MIPPaymentFormPhoto.photo, MIPPaymentFormPhoto.comments]
    column_sortable_list = [MIPPaymentFormPhoto.created_at]
    column_list = [MIPPaymentFormPhoto.id, MIPPaymentFormPhoto.mip_payment_form_id, MIPPaymentFormPhoto.photo, MIPPaymentFormPhoto.comments, MIPPaymentFormPhoto.is_deleted, MIPPaymentFormPhoto.created_at, MIPPaymentFormPhoto.updated_at]
    form_columns = [MIPPaymentFormPhoto.mip_payment_form_id, MIPPaymentFormPhoto.photo, MIPPaymentFormPhoto.comments, MIPPaymentFormPhoto.is_deleted]
