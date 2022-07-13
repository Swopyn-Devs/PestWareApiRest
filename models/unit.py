from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class Unit(Base):
    __tablename__ = 'units'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class UnitAdmin(ModelAdmin, model=Unit):
    column_searchable_list = [Unit.name]
    column_sortable_list = [Unit.created_at]
    column_list = [Unit.id, Unit.name, Unit.job_center_id, Unit.is_deleted, Unit.created_at, Unit.updated_at]
    form_columns = [Unit.name, Unit.job_center_id, Unit.is_deleted]
