from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class Status(Base):
    __tablename__ = 'status'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    key_string = Column(String, nullable=False)
    module = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class StatusAdmin(ModelAdmin, model=Status):
    column_searchable_list = [Status.name, Status.key_string, Status.module]
    column_sortable_list = [Status.created_at]
    column_list = [Status.id, Status.name, Status.key_string, Status.module, Status.is_active, Status.is_deleted, Status.created_at, Status.updated_at]
    form_columns = [Status.name, Status.key_string, Status.module, Status.is_active, Status.is_deleted]
