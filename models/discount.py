from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class Discount(Base):
    __tablename__ = 'discounts'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    percentage = Column(SmallInteger, nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class DiscountAdmin(ModelAdmin, model=Discount):
    column_searchable_list = [Discount.name, Discount.description]
    column_sortable_list = [Discount.created_at]
    column_list = [Discount.id, Discount.name, Discount.description, Discount.percentage, Discount.job_center_id, Discount.is_deleted, Discount.created_at, Discount.updated_at]
    form_columns = [Discount.name, Discount.description, Discount.percentage, Discount.job_center_id, Discount.is_deleted]
