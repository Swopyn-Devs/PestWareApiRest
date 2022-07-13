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

from sqladmin import Admin

from documentation.general import *
from schemas.auth import Settings
from utils.config import *
import routers

from database import engine
import models

app = FastAPI()
admin = Admin(
    app, 
    engine,
    base_url='/joxNjU3Nzc5ODk',
    logo_url='https://pwa-backend.s3.us-west-1.amazonaws.com/pestware-header-gray.png',
    title='Admin | Pestware REST'
)


admin.register_model(models.UserAdmin)
admin.register_model(models.EmployeeAdmin)
admin.register_model(models.CompanyAdmin)
admin.register_model(models.JobCenterAdmin)
admin.register_model(models.CustomerAdmin)
admin.register_model(models.CustomerPortalAccountAdmin)
admin.register_model(models.QuoteAdmin)
admin.register_model(models.QuotePlagueAdmin)
admin.register_model(models.QuoteConceptAdmin)
admin.register_model(models.QuoteExtraAdmin)
admin.register_model(models.QuoteTracingAdmin)
admin.register_model(models.RejectionReasonAdmin)
admin.register_model(models.CustomDescriptionAdmin)
admin.register_model(models.PriceListAdmin)
admin.register_model(models.PriceListPlagueAdmin)
admin.register_model(models.CountryAdmin)
admin.register_model(models.ApplicationMethodAdmin)
admin.register_model(models.BusinessActivityAdmin)
admin.register_model(models.CancellationReasonAdmin)
admin.register_model(models.CleaningAdmin)
admin.register_model(models.ConceptAdmin)
admin.register_model(models.DiscountAdmin)
admin.register_model(models.ExtraAdmin)
admin.register_model(models.IndicationAdmin)
admin.register_model(models.InfestationDegreeAdmin)
admin.register_model(models.JobTitleAdmin)
admin.register_model(models.OriginSourceAdmin)
admin.register_model(models.PaymentMethodAdmin)
admin.register_model(models.PaymentWayAdmin)
admin.register_model(models.PlagueCategoryAdmin)
admin.register_model(models.PlagueAdmin)
admin.register_model(models.PresentationAdmin)
admin.register_model(models.VoucherAdmin)
admin.register_model(models.StatusAdmin)
admin.register_model(models.TaxAdmin)
admin.register_model(models.TypeAdmin)
admin.register_model(models.ServiceTypeAdmin)
admin.register_model(models.SupplierAdmin)
admin.register_model(models.UnitAdmin)


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


app.include_router(routers.router)

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
