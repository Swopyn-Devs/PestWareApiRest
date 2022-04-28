from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base


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
