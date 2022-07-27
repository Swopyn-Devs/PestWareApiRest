from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class MIPInspectionFormPlague(Base):
    __tablename__ = 'mip_inspection_form_plague'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    mip_inspection_form_id = Column(UUID(as_uuid=True), nullable=False)
    plague_id = Column(UUID(as_uuid=True), nullable=False)
    infestation_degree_id = Column(UUID(as_uuid=True), nullable=False)
    nesting_area_id = Column(UUID(as_uuid=True), nullable=True)
    comments = Column(String, nullable=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class MIPInspectionFormPlagueAdmin(ModelAdmin, model=MIPInspectionFormPlague):
    column_searchable_list = [MIPInspectionFormPlague.comments]
    column_sortable_list = [MIPInspectionFormPlague.created_at]
    column_list = [MIPInspectionFormPlague.id, MIPInspectionFormPlague.mip_inspection_form_id, MIPInspectionFormPlague.plague_id, MIPInspectionFormPlague.infestation_degree_id, MIPInspectionFormPlague.nesting_area_id, MIPInspectionFormPlague.comments, MIPInspectionFormPlague.is_deleted, MIPInspectionFormPlague.created_at, MIPInspectionFormPlague.updated_at]
    form_columns = [MIPInspectionFormPlague.mip_inspection_form_id, MIPInspectionFormPlague.plague_id, MIPInspectionFormPlague.infestation_degree_id, MIPInspectionFormPlague.nesting_area_id, MIPInspectionFormPlague.comments, MIPInspectionFormPlague.is_deleted]
