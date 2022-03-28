from fastapi import FastAPI

from database import engine
from documentation.general import *
from models import user, company, employee
from routers import auth, companies, employees

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
employee.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(companies.router)
app.include_router(employees.router)
