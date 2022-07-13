from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    folio = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    contact_name = Column(String, nullable=True)
    contact_phone = Column(String, nullable=True)
    contact_email = Column(String, nullable=True)
    address = Column(String, nullable=True)
    address_latitude = Column(Numeric, nullable=True)
    address_longitude = Column(Numeric, nullable=True)
    is_main = Column(Boolean, default=True)
    main_customer_id = Column(UUID(as_uuid=True), nullable=True)
    business_activity_id = Column(UUID(as_uuid=True), nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class CustomerAdmin(ModelAdmin, model=Customer):
    column_searchable_list = [Customer.name, Customer.folio, Customer.phone, Customer.email, Customer.contact_name, Customer.address]
    column_sortable_list = [Customer.created_at]
    column_list = [Customer.id, Customer.name, Customer.folio, Customer.phone, Customer.contact_name, Customer.is_main, Customer.is_active, Customer.is_deleted, Customer.job_center_id, Customer.created_at, Customer.updated_at]
    form_columns = [Customer.name, Customer.folio, Customer.phone, Customer.email, Customer.contact_name, Customer.contact_phone, Customer.contact_email, Customer.address, Customer.address_latitude, Customer.address_longitude, Customer.is_main, Customer.main_customer_id, Customer.business_activity_id, Customer.job_center_id, Customer.is_active, Customer.is_deleted]
