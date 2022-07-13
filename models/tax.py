from email.policy import default
from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class Tax(Base):
    __tablename__ = 'taxes'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    value = Column(SmallInteger, nullable=False)
    is_main = Column(Boolean, default=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class TaxAdmin(ModelAdmin, model=Tax):
    column_searchable_list = [Tax.name]
    column_sortable_list = [Tax.created_at]
    column_list = [Tax.id, Tax.name, Tax.value, Tax.is_main, Tax.job_center_id, Tax.is_deleted, Tax.created_at, Tax.updated_at]
    form_columns = [Tax.name, Tax.value, Tax.is_main, Tax.is_deleted]
