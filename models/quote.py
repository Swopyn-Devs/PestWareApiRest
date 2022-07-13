from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID
import uuid

from database import Base


class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    folio = Column(String, nullable=False)
    quantity = Column(Integer, nullable=True)
    subtotal = Column(Numeric, nullable=False, default=0)
    discount = Column(Numeric, nullable=False, default=0)
    extra = Column(Numeric, nullable=False, default=0)
    tax = Column(Numeric, nullable=False, default=0)
    total = Column(Numeric, nullable=False, default=0)
    sent_mail = Column(Boolean, default=False)
    sent_whatsapp = Column(Boolean, default=False)
    approved = Column(Boolean, default=False)
    service_type_id = Column(UUID(as_uuid=True), nullable=False)
    customer_id = Column(UUID(as_uuid=True), nullable=False)
    origin_source_id = Column(UUID(as_uuid=True), nullable=True)
    discount_id = Column(UUID(as_uuid=True), nullable=True)
    employee_id = Column(UUID(as_uuid=True), nullable=False)
    price_list_id = Column(UUID(as_uuid=True), nullable=True)
    status_id = Column(UUID(as_uuid=True), nullable=False, default=uuid.UUID('8ba451f8-b352-4ff6-b573-532b36c7172b'))
    rejection_reason_id = Column(UUID(as_uuid=True), nullable=True)
    rejection_reason_comment = Column(String, nullable=True)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
