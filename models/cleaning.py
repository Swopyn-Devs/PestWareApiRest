from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class Cleaning(Base):
    __tablename__ = 'cleaning'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class CleaningAdmin(ModelAdmin, model=Cleaning):
    column_searchable_list = [Cleaning.name]
    column_sortable_list = [Cleaning.created_at]
    column_list = [Cleaning.id, Cleaning.name, Cleaning.job_center_id, Cleaning.is_deleted, Cleaning.created_at, Cleaning.updated_at]
    form_columns = [Cleaning.name, Cleaning.job_center_id, Cleaning.is_deleted]
