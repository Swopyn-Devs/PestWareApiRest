from sqlalchemy import *

from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL

from database import Base

import datetime


class Company(Base):
    __tablename__ = 'companies'

    id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    folio = Column(String, nullable=True)
    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    contact_name = Column(String, nullable=False)
    contact_email = Column(String, nullable=False)
    contact_phone = Column(String, nullable=False)
    country_id = Column(GUID, nullable=False)
    document_logo = Column(String, nullable=True)
    document_stamp = Column(String, nullable=True)
    web_logo = Column(String, nullable=True)
    web_color = Column(String, nullable=True)
    cutoff_date = Column(Date, nullable=True)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, onupdate=datetime.datetime.now)
    updated_at = Column(DateTime(timezone=True), server_default=func.now())
