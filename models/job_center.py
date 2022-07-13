from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class JobCenter(Base):
    __tablename__ = 'job_centers'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    business_name = Column(String, nullable=True)
    health_manager = Column(String, nullable=True)
    company_id = Column(UUID(as_uuid=True), nullable=False)
    taxpayer_registration = Column(String, nullable=True)
    license_number = Column(String, nullable=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    whatsapp = Column(String, nullable=True)
    web_page = Column(String, nullable=True)
    facebook = Column(String, nullable=True)
    messenger = Column(String, nullable=True)
    timezone = Column(String, default='America/Mexico_City')
    sanitary_license = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class JobCenterAdmin(ModelAdmin, model=JobCenter):
    column_searchable_list = [JobCenter.name, JobCenter.slug, JobCenter.health_manager, JobCenter.email, JobCenter.phone, JobCenter.license_number]
    column_sortable_list = [JobCenter.created_at]
    column_list = [JobCenter.id, JobCenter.name, JobCenter.business_name, JobCenter.company_id, JobCenter.license_number, JobCenter.is_active, JobCenter.is_deleted, JobCenter.created_at, JobCenter.updated_at]
    form_columns = [JobCenter.name, JobCenter.slug, JobCenter.business_name, JobCenter.health_manager, JobCenter.company_id, JobCenter.taxpayer_registration, JobCenter.license_number, JobCenter.email, JobCenter.phone, JobCenter.whatsapp, JobCenter.web_page, JobCenter.facebook, JobCenter.messenger, JobCenter.timezone, JobCenter.is_active, JobCenter.is_deleted]
