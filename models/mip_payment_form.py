from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID
import uuid

from database import Base
from sqladmin import ModelAdmin


class MIPPaymentForm(Base):
    __tablename__ = 'mip_payment_form'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    event_id = Column(UUID(as_uuid=True), nullable=False)
    payment_method_id = Column(UUID(as_uuid=True), nullable=False)
    payment_way_id = Column(UUID(as_uuid=True), nullable=False)
    amount = Column(Numeric, nullable=False, default=0)
    status_id = Column(UUID(as_uuid=True), nullable=False, default=uuid.UUID('8ba451f8-b352-4ff6-b573-532b36c7172b'))
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class MIPPaymentFormAdmin(ModelAdmin, model=MIPPaymentForm):
    column_sortable_list = [MIPPaymentForm.created_at]
    column_list = [MIPPaymentForm.id, MIPPaymentForm.event_id, MIPPaymentForm.payment_method_id, MIPPaymentForm.payment_way_id, MIPPaymentForm.amount, MIPPaymentForm.status_id, MIPPaymentForm.is_deleted, MIPPaymentForm.created_at, MIPPaymentForm.updated_at]
    form_columns = [MIPPaymentForm.event_id, MIPPaymentForm.payment_method_id, MIPPaymentForm.payment_way_id, MIPPaymentForm.amount, MIPPaymentForm.status_id, MIPPaymentForm.is_deleted]
