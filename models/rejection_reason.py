from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class RejectionReason(Base):
    __tablename__ = 'rejection_reasons'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class RejectionReasonAdmin(ModelAdmin, model=RejectionReason):
    column_searchable_list = [RejectionReason.name]
    column_sortable_list = [RejectionReason.created_at]
    column_list = [RejectionReason.id, RejectionReason.name, RejectionReason.job_center_id, RejectionReason.is_deleted, RejectionReason.created_at, RejectionReason.updated_at]
    form_columns = [RejectionReason.name, RejectionReason.job_center_id, RejectionReason.is_deleted]
