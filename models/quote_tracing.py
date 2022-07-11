from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base


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
