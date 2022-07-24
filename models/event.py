from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class Event(Base):
    __tablename__ = 'events'
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    title = Column(String, nullable=False)
    folio = Column(String, nullable=False)
    event_type_id = Column(UUID(as_uuid=True), nullable=False)
    initial_date = Column(Date, nullable=False)
    final_date = Column(Date, nullable=False)
    initial_hour = Column(Time, nullable=False)
    final_hour = Column(Time, nullable=False)
    real_initial_date = Column(Date, nullable=True)
    real_final_date = Column(Date, nullable=True)
    real_initial_hour = Column(Time, nullable=True)
    real_final_hour = Column(Time, nullable=True)
    start_latitude = Column(Numeric, nullable=True)
    start_longitude = Column(Numeric, nullable=True)
    end_latitude = Column(Numeric, nullable=True)
    end_longitude = Column(Numeric, nullable=True)
    quote_id = Column(UUID(as_uuid=True), nullable=True)
    customer_id = Column(UUID(as_uuid=True), nullable=True)
    employee_id = Column(UUID(as_uuid=True), nullable=True)
    service_type_id = Column(UUID(as_uuid=True), nullable=True)
    subtotal = Column(Numeric, nullable=True, default=0)
    discount = Column(Numeric, nullable=True, default=0)
    extra = Column(Numeric, nullable=True, default=0)
    tax = Column(Numeric, nullable=True, default=0)
    total = Column(Numeric, nullable=True, default=0)
    comments = Column(String, nullable=True)
    mip_inspection_form_id = Column(UUID(as_uuid=True), nullable=True)
    mip_condition_form_id = Column(UUID(as_uuid=True), nullable=True)
    mip_control_form_id = Column(UUID(as_uuid=True), nullable=True)
    mip_payment_form_id = Column(UUID(as_uuid=True), nullable=True)
    mip_signature_form_id = Column(UUID(as_uuid=True), nullable=True)
    status_id = Column(UUID(as_uuid=True), nullable=True)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())