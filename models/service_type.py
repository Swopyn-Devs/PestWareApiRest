from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base


class ServiceType(Base):
    __tablename__ = 'service_types'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    frequency_days = Column(SmallInteger, nullable=False)
    certificate_expiration_days = Column(SmallInteger, nullable=False)
    follow_up_days = Column(SmallInteger, nullable=False)
    disinfection = Column(Boolean, nullable=False, default=False)
    show_price = Column(Boolean, nullable=False, default=True)
    cover = Column(String, nullable=True)
    indication_id = Column(UUID(as_uuid=True), nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
