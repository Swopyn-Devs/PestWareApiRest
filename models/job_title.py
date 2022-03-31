import datetime

from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from sqlalchemy import *

from database import Base


class JobTitle(Base):
    __tablename__ = 'job_titles'

    id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    name = Column(String, nullable=False)
    job_center_id = Column(GUID, nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, onupdate=datetime.datetime.now)
    updated_at = Column(DateTime, server_default=func.now())
