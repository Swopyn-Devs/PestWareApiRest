from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    name = Column(String, nullable=False)
    company_id = Column(UUID(as_uuid=True), nullable=False)
    job_center_id = Column(UUID(as_uuid=True), nullable=False)
    job_title_id = Column(UUID(as_uuid=True), nullable=False)
    avatar = Column(String, nullable=True)
    signature = Column(String, nullable=True)
    color = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class EmployeeAdmin(ModelAdmin, model=Employee):
    column_searchable_list = [Employee.name]
    column_sortable_list = [Employee.created_at]
    column_list = [Employee.id, Employee.name, Employee.job_center_id, Employee.job_title_id, Employee.avatar, Employee.signature, Employee.color, Employee.is_active, Employee.is_deleted, Employee.created_at, Employee.updated_at]
    form_columns = [Employee.name, Employee.company_id, Employee.job_center_id, Employee.job_title_id, Employee.color, Employee.is_active, Employee.is_deleted]
