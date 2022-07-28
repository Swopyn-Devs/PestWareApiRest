from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class MIPInspectionForm(Base):
    __tablename__ = 'mip_inspection_form'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    event_id = Column(UUID(as_uuid=True), nullable=False)
    nesting_areas = Column(String, nullable=True)
    comments = Column(String, nullable=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class MIPInspectionFormAdmin(ModelAdmin, model=MIPInspectionForm):
    column_searchable_list = [MIPInspectionForm.nesting_areas, MIPInspectionForm.comments]
    column_sortable_list = [MIPInspectionForm.created_at]
    column_list = [MIPInspectionForm.id, MIPInspectionForm.event_id, MIPInspectionForm.nesting_areas, MIPInspectionForm.comments, MIPInspectionForm.is_deleted, MIPInspectionForm.created_at, MIPInspectionForm.updated_at]
    form_columns = [MIPInspectionForm.event_id, MIPInspectionForm.nesting_areas, MIPInspectionForm.comments, MIPInspectionForm.is_deleted]
