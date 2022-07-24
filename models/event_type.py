from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class EventType(Base):
    __tablename__ = 'event_types'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    quote_field = Column(Boolean, nullable=False, default=True)
    customer_field = Column(Boolean, nullable=False, default=False)
    employee_field = Column(Boolean, nullable=False, default=False)
    service_type_field = Column(Boolean, nullable=False, default=False)
    plagues_field = Column(Boolean, nullable=False, default=False)
    cost_field = Column(Boolean, nullable=False, default=False)
    comments_field = Column(Boolean, nullable=False, default=False)
    inspection_form = Column(Boolean, nullable=False, default=False)
    condition_form = Column(Boolean, nullable=False, default=False)
    control_form = Column(Boolean, nullable=False, default=False)
    payment_form = Column(Boolean, nullable=False, default=False)
    signature_form = Column(Boolean, nullable=False, default=False)
    notification_action = Column(Boolean, nullable=False, default=False)
    reminder_action = Column(Boolean, nullable=False, default=False)
    folio_key_setting = Column(String, nullable=False)
    folio_init_setting = Column(SmallInteger, nullable=False)
    is_service_order = Column(Boolean, nullable=False, default=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class EventTypeAdmin(ModelAdmin, model=EventType):
    column_searchable_list = [EventType.name]
    column_sortable_list = [EventType.created_at]
    column_list = [EventType.id, EventType.name, EventType.is_service_order, EventType.job_center_id, EventType.is_deleted, EventType.created_at, EventType.updated_at]
    form_columns = [
        EventType.name,
        EventType.quote_field,
        EventType.customer_field,
        EventType.employee_field,
        EventType.service_type_field,
        EventType.plagues_field,
        EventType.cost_field,
        EventType.comments_field,
        EventType.inspection_form,
        EventType.condition_form,
        EventType.condition_form,
        EventType.payment_form,
        EventType.signature_form,
        EventType.notification_action,
        EventType.reminder_action,
        EventType.folio_key_setting,
        EventType.folio_init_setting,
        EventType.is_service_order,
        EventType.job_center_id,
        EventType.is_deleted
    ]
