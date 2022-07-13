from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class Voucher(Base):
    __tablename__ = 'vouchers'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class VoucherAdmin(ModelAdmin, model=Voucher):
    column_searchable_list = [Voucher.name]
    column_sortable_list = [Voucher.created_at]
    column_list = [Voucher.id, Voucher.name, Voucher.job_center_id, Voucher.is_deleted, Voucher.created_at, Voucher.updated_at]
    form_columns = [Voucher.name, Voucher.job_center_id, Voucher.is_deleted]
