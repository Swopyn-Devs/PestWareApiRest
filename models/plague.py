from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class Plague(Base):
    __tablename__ = 'plagues'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    plague_category_id = Column(UUID(as_uuid=True), nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class PlagueAdmin(ModelAdmin, model=Plague):
    column_searchable_list = [Plague.name]
    column_sortable_list = [Plague.created_at]
    column_list = [Plague.id, Plague.name, Plague.plague_category_id, Plague.job_center_id, Plague.is_deleted, Plague.created_at, Plague.updated_at]
    form_columns = [Plague.name, Plague.plague_category_id, Plague.job_center_id, Plague.is_deleted]
