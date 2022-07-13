from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class QuotePlague(Base):
    __tablename__ = 'quote_plagues'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    quote_id = Column(UUID(as_uuid=True), nullable=False)
    plague_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class QuotePlagueAdmin(ModelAdmin, model=QuotePlague):
    column_sortable_list = [QuotePlague.created_at]
    column_list = [QuotePlague.id, QuotePlague.quote_id, QuotePlague.plague_id, QuotePlague.is_deleted, QuotePlague.created_at, QuotePlague.updated_at]
    form_columns = [QuotePlague.quote_id, QuotePlague.plague_id, QuotePlague.is_deleted]
