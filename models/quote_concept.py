from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base


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
