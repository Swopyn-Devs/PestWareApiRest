from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

from database import Base
from sqladmin import ModelAdmin


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=DefaultClause(text('gen_random_uuid()')))
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    employee_id = Column(UUID(as_uuid=True), nullable=True)
    confirmation_code = Column(String, nullable=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class UserAdmin(ModelAdmin, model=User):
    column_searchable_list = [User.email]
    column_sortable_list = [User.created_at]
    column_list = [User.id, User.email, User.is_verified, User.is_active, User.is_deleted, User.confirmation_code, User.employee_id, User.created_at, User.updated_at]
    form_columns = [User.email, User.password, User.is_verified, User.is_active, User.employee_id, User.confirmation_code, User.is_deleted]
