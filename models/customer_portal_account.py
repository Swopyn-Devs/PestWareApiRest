from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base


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
