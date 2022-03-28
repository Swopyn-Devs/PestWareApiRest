from fastapi import FastAPI

from database import engine
from documentation.general import *
from models import user, company
from routers import auth

app = FastAPI(
    title="PestWare App API REST",
    description=description,
    version=version,
    terms_of_service=terms_of_service,
    contact=contact,
    license_info=license_info
)

user.Base.metadata.create_all(bind=engine)
company.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
