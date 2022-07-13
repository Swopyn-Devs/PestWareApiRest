import imp
from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class Extra(Base):
    __tablename__ = 'extras'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class ExtraAdmin(ModelAdmin, model=Extra):
    column_searchable_list = [Extra.name, Extra.description]
    column_sortable_list = [Extra.created_at]
    column_list = [Extra.id, Extra.name, Extra.description, Extra.quantity, Extra.job_center_id, Extra.is_deleted, Extra.created_at, Extra.updated_at]
    form_columns = [Extra.name, Extra.description, Extra.quantity, Extra.job_center_id, Extra.is_deleted]
