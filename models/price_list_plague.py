from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class PriceListPlague(Base):
    __tablename__ = 'price_list_plagues'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    price_list_id = Column(UUID(as_uuid=True), nullable=False)
    plague_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class PriceListPlagueAdmin(ModelAdmin, model=PriceListPlague):
    column_sortable_list = [PriceListPlague.created_at]
    column_list = [PriceListPlague.id, PriceListPlague.price_list_id, PriceListPlague.plague_id, PriceListPlague.is_deleted, PriceListPlague.created_at, PriceListPlague.updated_at]
    form_columns = [PriceListPlague.price_list_id, PriceListPlague.plague_id, PriceListPlague.is_deleted]
