from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class OriginSource(Base):
    __tablename__ = 'origin_sources'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class OriginSourceAdmin(ModelAdmin, model=OriginSource):
    column_searchable_list = [OriginSource.name]
    column_sortable_list = [OriginSource.created_at]
    column_list = [OriginSource.id, OriginSource.name, OriginSource.job_center_id, OriginSource.is_deleted, OriginSource.created_at, OriginSource.updated_at]
    form_columns = [OriginSource.name, OriginSource.job_center_id, OriginSource.is_deleted]
