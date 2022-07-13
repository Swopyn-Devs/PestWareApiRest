from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class QuoteTracing(Base):
    __tablename__ = 'quote_tracing'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    quote_id = Column(UUID(as_uuid=True), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    comment = Column(String, nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class QuoteTracingAdmin(ModelAdmin, model=QuoteTracing):
    column_searchable_list = [QuoteTracing.date, QuoteTracing.time, QuoteTracing.comment]
    column_sortable_list = [QuoteTracing.created_at]
    column_list = [QuoteTracing.id, QuoteTracing.quote_id, QuoteTracing.date, QuoteTracing.time, QuoteTracing.comment, QuoteTracing.is_deleted, QuoteTracing.created_at, QuoteTracing.updated_at]
    form_columns = [QuoteTracing.quote_id, QuoteTracing.date, QuoteTracing.time, QuoteTracing.comment, QuoteTracing.is_deleted]
