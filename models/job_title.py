from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class JobTitle(Base):
    __tablename__ = 'job_titles'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class JobTitleAdmin(ModelAdmin, model=JobTitle):
    column_searchable_list = [JobTitle.name]
    column_sortable_list = [JobTitle.created_at]
    column_list = [JobTitle.id, JobTitle.name, JobTitle.job_center_id, JobTitle.is_deleted, JobTitle.created_at, JobTitle.updated_at]
    form_columns = [JobTitle.name, JobTitle.job_center_id, JobTitle.is_deleted]
