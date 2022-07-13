from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    contact_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    bank = Column(String, nullable=False)
    account_holder = Column(String, nullable=False)
    account_number = Column(String, nullable=False)
    taxpayer_registration = Column(String, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class SupplierAdmin(ModelAdmin, model=Supplier):
    column_searchable_list = [Supplier.name, Supplier.contact_name, Supplier.address, Supplier.phone, Supplier.email, Supplier.bank, Supplier.account_holder, Supplier.account_number, Supplier.taxpayer_registration]
    column_sortable_list = [Supplier.created_at]
    column_list = [Supplier.id, Supplier.name, Supplier.contact_name, Supplier.job_center_id, Supplier.is_deleted, Supplier.created_at, Supplier.updated_at]
    form_columns = [Supplier.name, Supplier.contact_name, Supplier.address, Supplier.phone, Supplier.email, Supplier.bank, Supplier.account_holder, Supplier.account_number, Supplier.taxpayer_registration, Supplier.job_center_id, Supplier.is_deleted]
