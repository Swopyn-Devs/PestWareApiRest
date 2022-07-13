from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class CancellationReason(Base):
    __tablename__ = 'cancellation_reasons'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class CancellationReasonAdmin(ModelAdmin, model=CancellationReason):
    column_searchable_list = [CancellationReason.name]
    column_sortable_list = [CancellationReason.created_at]
    column_list = [CancellationReason.id, CancellationReason.name, CancellationReason.job_center_id, CancellationReason.is_deleted, CancellationReason.created_at, CancellationReason.updated_at]
    form_columns = [CancellationReason.name, CancellationReason.job_center_id, CancellationReason.is_deleted]
