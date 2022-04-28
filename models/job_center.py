from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base


class JobCenter(Base):
    __tablename__ = 'job_centers'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
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
