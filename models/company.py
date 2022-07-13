from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class Company(Base):
    __tablename__ = 'companies'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    folio = Column(String, nullable=True)
    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    contact_name = Column(String, nullable=False)
    contact_email = Column(String, nullable=False)
    contact_phone = Column(String, nullable=False)
    country_id = Column(UUID(as_uuid=True), nullable=False)
    document_logo = Column(String, nullable=True)
    document_stamp = Column(String, nullable=True)
    web_logo = Column(String, nullable=True)
    web_color = Column(String, nullable=True)
    cutoff_date = Column(Date, nullable=True)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class CompanyAdmin(ModelAdmin, model=Company):
    column_searchable_list = [Company.name, Company.folio, Company.slug]
    column_sortable_list = [Company.created_at]
    column_list = [Company.id, Company.folio, Company.name, Company.contact_name, Company.cutoff_date, Company.is_deleted, Company.created_at, Company.updated_at]
    form_columns = [Company.folio, Company.name, Company.slug, Company.contact_name, Company.contact_email, Company.contact_phone, Company.country_id, Company.cutoff_date, Company.is_active, Company.is_deleted]
