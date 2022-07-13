from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class QuoteConcept(Base):
    __tablename__ = 'quote_concepts'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    quote_id = Column(UUID(as_uuid=True), nullable=False)
    concept = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    unit_price = Column(Numeric, nullable=False, default=0)
    subtotal = Column(Numeric, nullable=False, default=0)
    total = Column(Numeric, nullable=False, default=0)
    tax = Column(Numeric, nullable=False, default=0)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class QuoteConceptAdmin(ModelAdmin, model=QuoteConcept):
    column_searchable_list = [QuoteConcept.concept]
    column_sortable_list = [QuoteConcept.created_at]
    column_list = [QuoteConcept.id, QuoteConcept.quote_id, QuoteConcept.concept, QuoteConcept.quantity, QuoteConcept.unit_price, QuoteConcept.subtotal, QuoteConcept.tax, QuoteConcept.total, QuoteConcept.is_deleted, QuoteConcept.created_at, QuoteConcept.updated_at]
    form_columns = [QuoteConcept.quote_id, QuoteConcept.concept, QuoteConcept.quantity, QuoteConcept.unit_price, QuoteConcept.subtotal, QuoteConcept.tax, QuoteConcept.total, QuoteConcept.is_deleted]
