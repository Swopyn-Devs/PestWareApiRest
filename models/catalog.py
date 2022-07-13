from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class Country(Base):
    __tablename__ = 'countries'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    code_country = Column(String, nullable=False)
    coin_country = Column(String, nullable=False)
    symbol_country = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class CountryAdmin(ModelAdmin, model=Country):
    column_searchable_list = [Country.id, Country.name]
    column_sortable_list = [Country.created_at]
    column_list = [Country.id, Country.name, Country.is_active, Country.is_deleted, Country.created_at, Country.updated_at]
    form_columns = [Country.name, Country.code_country, Country.coin_country, Country.symbol_country, Country.is_active, Country.is_deleted]
