from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base


class PriceList(Base):
    __tablename__ = 'price_list'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    key = Column(String, nullable=False)
    hierarchy = Column(SmallInteger, nullable=False)
    cost = Column(Numeric, nullable=False)
    min_cost = Column(Numeric, nullable=False)
    service_type_id = Column(UUID(as_uuid=True), nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
