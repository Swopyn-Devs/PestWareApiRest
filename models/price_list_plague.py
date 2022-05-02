from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base


class PriceListPlague(Base):
    __tablename__ = 'price_list_plagues'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    price_list_id = Column(UUID(as_uuid=True), primary_key=True)
    plague_id = Column(UUID(as_uuid=True), primary_key=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
