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


class EventAdmin(ModelAdmin, model=Event):
    column_searchable_list = [Event.title, Event.folio]
    column_sortable_list = [Event.created_at]
    column_list = [Event.id, Event.title, Event.folio, Event.job_center_id, Event.is_deleted, Event.created_at, Event.updated_at]
    form_columns = [
        Event.title,
        Event.folio,
        Event.event_type_id,
        Event.initial_date,
        Event.final_date,
        Event.initial_hour,
        Event.final_hour,
        Event.real_initial_date,
        Event.real_final_date,
        Event.real_initial_hour,
        Event.real_final_hour,
        Event.start_latitude,
        Event.start_longitude,
        Event.end_latitude,
        Event.end_longitude,
        Event.quote_id,
        Event.customer_id,
        Event.employee_id,
        Event.service_type_id,
        Event.subtotal,
        Event.discount,
        Event.extra,
        Event.tax,
        Event.total,
        Event.comments,
        Event.mip_inspection_form_id,
        Event.mip_condition_form_id,
        Event.mip_control_form_id,
        Event.mip_payment_form_id,
        Event.mip_signature_form_id,
        Event.status_id,
        Event.job_center_id,
        Event.is_deleted
    ]
