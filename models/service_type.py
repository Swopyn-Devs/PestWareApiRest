from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


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


class ServiceTypeAdmin(ModelAdmin, model=ServiceType):
    column_searchable_list = [ServiceType.name]
    column_sortable_list = [ServiceType.created_at]
    column_list = [ServiceType.id, ServiceType.name, ServiceType.frequency_days, ServiceType.certificate_expiration_days, ServiceType.follow_up_days, ServiceType.disinfection, ServiceType.show_price, ServiceType.cover, ServiceType.job_center_id, ServiceType.is_deleted, ServiceType.created_at, ServiceType.updated_at]
    form_columns = [ServiceType.name, ServiceType.frequency_days, ServiceType.certificate_expiration_days, ServiceType.follow_up_days, ServiceType.disinfection, ServiceType.show_price, ServiceType.indication_id, ServiceType.job_center_id, ServiceType.is_deleted]
