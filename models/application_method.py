from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class ApplicationMethod(Base):
    __tablename__ = 'application_methods'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class ApplicationMethodAdmin(ModelAdmin, model=ApplicationMethod):
    column_searchable_list = [ApplicationMethod.name]
    column_sortable_list = [ApplicationMethod.created_at]
    column_list = [ApplicationMethod.id, ApplicationMethod.name, ApplicationMethod.job_center_id, ApplicationMethod.is_deleted, ApplicationMethod.created_at, ApplicationMethod.updated_at]
    form_columns = [ApplicationMethod.name, ApplicationMethod.job_center_id, ApplicationMethod.is_deleted]
