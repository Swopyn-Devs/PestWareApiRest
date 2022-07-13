from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class BusinessActivity(Base):
    __tablename__ = 'business_activities'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class BusinessActivityAdmin(ModelAdmin, model=BusinessActivity):
    column_searchable_list = [BusinessActivity.name]
    column_sortable_list = [BusinessActivity.created_at]
    column_list = [BusinessActivity.id, BusinessActivity.name, BusinessActivity.job_center_id, BusinessActivity.is_deleted, BusinessActivity.created_at, BusinessActivity.updated_at]
    form_columns = [BusinessActivity.name, BusinessActivity.job_center_id, BusinessActivity.is_deleted]
