from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class MIPConditionFormCleaning(Base):
    __tablename__ = 'mip_condition_form_cleaning'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    mip_condition_form_id = Column(UUID(as_uuid=True), nullable=False)
    cleaning_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class MIPConditionFormCleaningAdmin(ModelAdmin, model=MIPConditionFormCleaning):
    column_sortable_list = [MIPConditionFormCleaning.created_at]
    column_list = [MIPConditionFormCleaning.id, MIPConditionFormCleaning.mip_condition_form_id, MIPConditionFormCleaning.cleaning_id, MIPConditionFormCleaning.is_deleted, MIPConditionFormCleaning.created_at, MIPConditionFormCleaning.updated_at]
    form_columns = [MIPConditionFormCleaning.mip_condition_form_id, MIPConditionFormCleaning.cleaning_id, MIPConditionFormCleaning.is_deleted]
