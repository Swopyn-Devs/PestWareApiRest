from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class Presentation(Base):
    __tablename__ = 'presentations'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class PresentationAdmin(ModelAdmin, model=Presentation):
    column_searchable_list = [Presentation.name]
    column_sortable_list = [Presentation.created_at]
    column_list = [Presentation.id, Presentation.name, Presentation.job_center_id, Presentation.is_deleted, Presentation.created_at, Presentation.updated_at]
    form_columns = [Presentation.name, Presentation.job_center_id, Presentation.is_deleted]
