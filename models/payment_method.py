from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class PaymentMethod(Base):
    __tablename__ = 'payment_methods'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class PaymentMethodAdmin(ModelAdmin, model=PaymentMethod):
    column_searchable_list = [PaymentMethod.name]
    column_sortable_list = [PaymentMethod.created_at]
    column_list = [PaymentMethod.id, PaymentMethod.name, PaymentMethod.job_center_id, PaymentMethod.is_deleted, PaymentMethod.created_at, PaymentMethod.updated_at]
    form_columns = [PaymentMethod.name, PaymentMethod.job_center_id, PaymentMethod.is_deleted]
