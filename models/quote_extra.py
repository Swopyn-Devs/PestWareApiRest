from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class QuoteExtra(Base):
    __tablename__ = 'quote_extras'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    quote_id = Column(UUID(as_uuid=True), nullable=False)
    extra_id = Column(UUID(as_uuid=True), nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class QuoteExtraAdmin(ModelAdmin, model=QuoteExtra):
    column_sortable_list = [QuoteExtra.created_at]
    column_list = [QuoteExtra.id, QuoteExtra.quote_id, QuoteExtra.extra_id, QuoteExtra.quantity, QuoteExtra.is_deleted, QuoteExtra.created_at, QuoteExtra.updated_at]
    form_columns = [QuoteExtra.quote_id, QuoteExtra.extra_id, QuoteExtra.quantity, QuoteExtra.is_deleted]
