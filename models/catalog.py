from sqlalchemy import *

from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL

from database import Base

import datetime


class Country(Base):
    __tablename__ = 'countries'

    id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    name = Column(String, nullable=False)
    code_country = Column(String, nullable=False)
    coin_country = Column(String, nullable=False)
    symbol_country = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, onupdate=datetime.datetime.now)
    updated_at = Column(DateTime, server_default=func.now())
