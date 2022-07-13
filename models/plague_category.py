from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class PlagueCategory(Base):
    __tablename__ = 'plague_categories'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class PlagueCategoryAdmin(ModelAdmin, model=PlagueCategory):
    column_searchable_list = [PlagueCategory.name]
    column_sortable_list = [PlagueCategory.created_at]
    column_list = [PlagueCategory.id, PlagueCategory.name, PlagueCategory.job_center_id, PlagueCategory.is_deleted, PlagueCategory.created_at, PlagueCategory.updated_at]
    form_columns = [PlagueCategory.name, PlagueCategory.job_center_id, PlagueCategory.is_deleted]
