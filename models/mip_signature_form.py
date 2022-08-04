from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class MIPSignatureForm(Base):
    __tablename__ = 'mip_signature_form'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    event_id = Column(UUID(as_uuid=True), nullable=False)
    signature = Column(String, nullable=False)
    name = Column(String, nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class MIPSignatureFormAdmin(ModelAdmin, model=MIPSignatureForm):
    column_searchable_list = [MIPSignatureForm.signature, MIPSignatureForm.name]
    column_sortable_list = [MIPSignatureForm.created_at]
    column_list = [MIPSignatureForm.id, MIPSignatureForm.event_id, MIPSignatureForm.signature, MIPSignatureForm.name, MIPSignatureForm.is_deleted, MIPSignatureForm.created_at, MIPSignatureForm.updated_at]
    form_columns = [MIPSignatureForm.event_id, MIPSignatureForm.signature, MIPSignatureForm.name, MIPSignatureForm.is_deleted]
