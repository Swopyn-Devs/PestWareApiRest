from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class MIPConditionFormPhoto(Base):
    __tablename__ = 'mip_condition_form_photo'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    mip_condition_form_id = Column(UUID(as_uuid=True), nullable=False)
    photo = Column(String, nullable=False)
    comments = Column(String, nullable=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class MIPConditionFormPhotoAdmin(ModelAdmin, model=MIPConditionFormPhoto):
    column_searchable_list = [MIPConditionFormPhoto.photo, MIPConditionFormPhoto.comments]
    column_sortable_list = [MIPConditionFormPhoto.created_at]
    column_list = [MIPConditionFormPhoto.id, MIPConditionFormPhoto.mip_condition_form_id, MIPConditionFormPhoto.photo, MIPConditionFormPhoto.comments, MIPConditionFormPhoto.is_deleted, MIPConditionFormPhoto.created_at, MIPConditionFormPhoto.updated_at]
    form_columns = [MIPConditionFormPhoto.mip_condition_form_id, MIPConditionFormPhoto.photo, MIPConditionFormPhoto.comments, MIPConditionFormPhoto.is_deleted]
