from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class PaymentWay(Base):
    __tablename__ = 'payment_ways'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    credit_days = Column(SmallInteger, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class PaymentWayAdmin(ModelAdmin, model=PaymentWay):
    column_searchable_list = [PaymentWay.name]
    column_sortable_list = [PaymentWay.created_at]
    column_list = [PaymentWay.id, PaymentWay.name, PaymentWay.credit_days, PaymentWay.job_center_id, PaymentWay.is_deleted, PaymentWay.created_at, PaymentWay.updated_at]
    form_columns = [PaymentWay.name, PaymentWay.credit_days, PaymentWay.job_center_id, PaymentWay.is_deleted]
