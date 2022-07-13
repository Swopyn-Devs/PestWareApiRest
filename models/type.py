from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class Type(Base):
    __tablename__ = 'types'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class TypeAdmin(ModelAdmin, model=Type):
    column_searchable_list = [Type.name]
    column_sortable_list = [Type.created_at]
    column_list = [Type.id, Type.name, Type.job_center_id, Type.is_deleted, Type.created_at, Type.updated_at]
    form_columns = [Type.name, Type.job_center_id, Type.is_deleted]
