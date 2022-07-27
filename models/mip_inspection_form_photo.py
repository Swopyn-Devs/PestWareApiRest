from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class MIPInspectionFormPhoto(Base):
    __tablename__ = 'mip_inspection_form_photo'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    mip_inspection_form_id = Column(UUID(as_uuid=True), nullable=False)
    photo = Column(String, nullable=False)
    comments = Column(String, nullable=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class MIPInspectionFormPhotoAdmin(ModelAdmin, model=MIPInspectionFormPhoto):
    column_searchable_list = [MIPInspectionFormPhoto.photo, MIPInspectionFormPhoto.comments]
    column_sortable_list = [MIPInspectionFormPhoto.created_at]
    column_list = [MIPInspectionFormPhoto.id, MIPInspectionFormPhoto.mip_inspection_form_id, MIPInspectionFormPhoto.photo, MIPInspectionFormPhoto.comments, MIPInspectionFormPhoto.is_deleted, MIPInspectionFormPhoto.created_at, MIPInspectionFormPhoto.updated_at]
    form_columns = [MIPInspectionFormPhoto.mip_inspection_form_id, MIPInspectionFormPhoto.photo, MIPInspectionFormPhoto.comments, MIPInspectionFormPhoto.is_deleted]
