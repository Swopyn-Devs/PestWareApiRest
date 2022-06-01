from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base


class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    folio = Column(String, nullable=False)
    total = Column(Numeric, nullable=False)
    description = Column(String, nullable=True)
    service_type_id = Column(UUID(as_uuid=True), nullable=False)
    customer_id = Column(UUID(as_uuid=True), nullable=False)
    origin_source_id = Column(UUID(as_uuid=True), nullable=False)
    employee_id = Column(UUID(as_uuid=True), nullable=False)
    status_id = Column(UUID(as_uuid=True), nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
