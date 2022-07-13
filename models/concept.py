from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class Concept(Base):
    __tablename__ = 'concepts'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class ConceptAdmin(ModelAdmin, model=Concept):
    column_searchable_list = [Concept.name, Concept.type]
    column_sortable_list = [Concept.created_at]
    column_list = [Concept.id, Concept.name, Concept.type, Concept.job_center_id, Concept.is_deleted, Concept.created_at, Concept.updated_at]
    form_columns = [Concept.name, Concept.type, Concept.job_center_id, Concept.is_deleted]
