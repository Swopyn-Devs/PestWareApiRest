from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class NestingArea(Base):
    __tablename__ = 'nesting_areas'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    customer_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class NestingAreaAdmin(ModelAdmin, model=NestingArea):
    column_searchable_list = [NestingArea.name]
    column_sortable_list = [NestingArea.created_at]
    column_list = [NestingArea.id, NestingArea.name, NestingArea.customer_id, NestingArea.is_deleted, NestingArea.created_at, NestingArea.updated_at]
    form_columns = [NestingArea.name, NestingArea.customer_id, NestingArea.is_deleted]
