import datetime

from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from sqlalchemy import *

from database import Base


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    name = Column(String, nullable=False)
    company_id = Column(GUID, nullable=False)
    job_center_id = Column(GUID, nullable=False)
    job_title_id = Column(GUID, nullable=False)
    avatar = Column(String, nullable=True)
    signature = Column(String, nullable=True)
    color = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, onupdate=datetime.datetime.now)
    updated_at = Column(DateTime, server_default=func.now())
