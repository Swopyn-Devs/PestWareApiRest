from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class CustomDescription(Base):
    __tablename__ = 'custom_descriptions'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class CustomDescriptionAdmin(ModelAdmin, model=CustomDescription):
    column_searchable_list = [CustomDescription.name, CustomDescription.description]
    column_sortable_list = [CustomDescription.created_at]
    column_list = [CustomDescription.id, CustomDescription.name, CustomDescription.description, CustomDescription.job_center_id, CustomDescription.is_deleted, CustomDescription.created_at, CustomDescription.updated_at]
    form_columns = [CustomDescription.name, CustomDescription.description, CustomDescription.job_center_id, CustomDescription.is_deleted]
