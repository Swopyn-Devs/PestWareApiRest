from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class InfestationDegree(Base):
    __tablename__ = 'infestation_degrees'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class InfestationDegreeAdmin(ModelAdmin, model=InfestationDegree):
    column_searchable_list = [InfestationDegree.name]
    column_sortable_list = [InfestationDegree.created_at]
    column_list = [InfestationDegree.id, InfestationDegree.name, InfestationDegree.job_center_id, InfestationDegree.is_deleted, InfestationDegree.created_at, InfestationDegree.updated_at]
    form_columns = [InfestationDegree.name, InfestationDegree.job_center_id, InfestationDegree.is_deleted]
