from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class MIPConditionForm(Base):
    __tablename__ = 'mip_condition_form'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    event_id = Column(UUID(as_uuid=True), nullable=False)
    indications = Column(Boolean, nullable=False, default=False)
    restricted_access = Column(String, nullable=True)
    comments = Column(String, nullable=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class MIPConditionFormAdmin(ModelAdmin, model=MIPConditionForm):
    column_searchable_list = [MIPConditionForm.restricted_access, MIPConditionForm.comments]
    column_sortable_list = [MIPConditionForm.created_at]
    column_list = [MIPConditionForm.id, MIPConditionForm.event_id, MIPConditionForm.indications, MIPConditionForm.restricted_access, MIPConditionForm.comments, MIPConditionForm.is_deleted, MIPConditionForm.created_at, MIPConditionForm.updated_at]
    form_columns = [MIPConditionForm.event_id, MIPConditionForm.indications, MIPConditionForm.restricted_access, MIPConditionForm.comments, MIPConditionForm.is_deleted]
