from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from documentation.general import *

from models import user, company, employee, catalog, job_title
from routers import auth, companies, employees, catalogs, job_titles
from schemas.auth import Settings

app = FastAPI(
    title="PestWare App API REST",
    description=description,
    version=version,
    terms_of_service=terms_of_service,
    contact=contact,
    license_info=license_info
)

origins = [
    'http://localhost',
    'http://localhost:4200',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user.Base.metadata.create_all(bind=engine)
company.Base.metadata.create_all(bind=engine)
employee.Base.metadata.create_all(bind=engine)
catalog.Base.metadata.create_all(bind=engine)
job_title.Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(companies.router)
app.include_router(employees.router)
app.include_router(catalogs.router)
app.include_router(job_titles.router)
