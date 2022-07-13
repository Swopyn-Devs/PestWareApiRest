from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class Indication(Base):
    __tablename__ = 'indications'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    key = Column(String, nullable=False)
    description = Column(String, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class IndicationAdmin(ModelAdmin, model=Indication):
    column_searchable_list = [Indication.name, Indication.key, Indication.description]
    column_sortable_list = [Indication.created_at]
    column_list = [Indication.id, Indication.name, Indication.key, Indication.description, Indication.job_center_id, Indication.is_deleted, Indication.created_at, Indication.updated_at]
    form_columns = [Indication.name, Indication.key, Indication.description, Indication.job_center_id, Indication.is_deleted]
