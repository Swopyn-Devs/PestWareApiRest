from sqlalchemy import *

from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL

from database import Base

import datetime


class User(Base):
    __tablename__ = 'users'

    id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    employee_id = Column(GUID, nullable=True)
    confirmation_code = Column(String, nullable=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, onupdate=datetime.datetime.now)
    updated_at = Column(DateTime, server_default=func.now())
