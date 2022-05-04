from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base


class PriceListPrice(Base):
    __tablename__ = 'price_list_prices'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    price_list_id = Column(UUID(as_uuid=True), primary_key=True)
    scale = Column(Integer, nullable=False)
    price_one = Column(SmallInteger, nullable=False)
    price_two = Column(SmallInteger, nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
