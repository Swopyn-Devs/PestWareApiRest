from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class CustomerPortalAccount(Base):
    __tablename__ = 'customer_portal_accounts'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    customer_id = Column(UUID(as_uuid=True), nullable=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class CustomerPortalAccountAdmin(ModelAdmin, model=CustomerPortalAccount):
    column_searchable_list = [CustomerPortalAccount.name, CustomerPortalAccount.username]
    column_sortable_list = [CustomerPortalAccount.created_at]
    column_list = [CustomerPortalAccount.id, CustomerPortalAccount.name, CustomerPortalAccount.username, CustomerPortalAccount.customer_id, CustomerPortalAccount.is_active, CustomerPortalAccount.is_deleted, CustomerPortalAccount.created_at, CustomerPortalAccount.updated_at]
    form_columns = [CustomerPortalAccount.name, CustomerPortalAccount.username, CustomerPortalAccount.password, CustomerPortalAccount.is_active, CustomerPortalAccount.customer_id, CustomerPortalAccount.is_deleted]
