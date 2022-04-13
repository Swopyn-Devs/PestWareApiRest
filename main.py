import inspect
import re

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi_pagination import add_pagination

from database import engine
from documentation.general import *
from models import user, company, employee, catalog, job_title, tax, payment_way, payment_method, voucher, concept, presentation, type, unit
from routers import auth, companies, employees, catalogs, job_titles, taxes, payment_ways, payment_methods, vouchers, concepts, presentations, types, units
from schemas.auth import Settings
from utils.config import *

app = FastAPI()


@AuthJWT.load_config
def get_config():
    return Settings()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    print(request)
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


origins = origins

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
tax.Base.metadata.create_all(bind=engine)
payment_way.Base.metadata.create_all(bind=engine)
payment_method.Base.metadata.create_all(bind=engine)
voucher.Base.metadata.create_all(bind=engine)
concept.Base.metadata.create_all(bind=engine)
presentation.Base.metadata.create_all(bind=engine)
type.Base.metadata.create_all(bind=engine)
unit.Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(companies.router)
app.include_router(employees.router)
app.include_router(catalogs.router)
app.include_router(job_titles.router)
app.include_router(taxes.router)
app.include_router(payment_ways.router)
app.include_router(payment_methods.router)
app.include_router(vouchers.router)
app.include_router(concepts.router)
app.include_router(presentations.router)
app.include_router(types.router)
app.include_router(units.router)

add_pagination(app)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="PestWare App API REST",
        description=description,
        version=version,
        terms_of_service=terms_of_service,
        contact=contact,
        license_info=license_info,
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "Bearer Auth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Enter: **'Bearer &lt;JWT&gt;'**, where JWT is the access token"
        }
    }

    # Get all routes where jwt_optional() or jwt_required
    api_router = [route for route in app.routes if isinstance(route, APIRoute)]

    for route in api_router:
        path = getattr(route, "path")
        endpoint = getattr(route, "endpoint")
        methods = [method.lower() for method in getattr(route, "methods")]

        for method in methods:
            # access_token
            if (
                    re.search("jwt_required", inspect.getsource(endpoint)) or
                    re.search("fresh_jwt_required", inspect.getsource(endpoint)) or
                    re.search("jwt_optional", inspect.getsource(endpoint))
            ):
                openapi_schema["paths"][path][method]["security"] = [
                    {
                        "Bearer Auth": []
                    }
                ]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
