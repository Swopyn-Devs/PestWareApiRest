from fastapi import APIRouter

from routers import application_methods
from routers import auth
from routers import cancellation_reasons
from routers import catalogs
from routers import cleaning
from routers import companies
from routers import concepts
from routers import custom_descriptions
from routers import customers
from routers import discounts
from routers import employees
from routers import extras
from routers import indications
from routers import infestation_degrees
from routers import job_centers
from routers import job_titles
from routers import origin_sources
from routers import payment_methods
from routers import payment_ways
from routers import plague_categories
from routers import plagues
from routers import presentations
from routers import rejection_reasons
from routers import service_types
from routers import taxes
from routers import types
from routers import units
from routers import vouchers
from routers import price_lists
from routers import suppliers
from routers import status as status_router
from routers import quotes

router = APIRouter()

router.include_router(auth.router)
router.include_router(companies.router)
router.include_router(job_centers.router)
router.include_router(employees.router)
router.include_router(customers.router)
router.include_router(catalogs.router)
router.include_router(job_titles.router)
router.include_router(taxes.router)
router.include_router(payment_ways.router)
router.include_router(payment_methods.router)
router.include_router(vouchers.router)
router.include_router(concepts.router)
router.include_router(presentations.router)
router.include_router(types.router)
router.include_router(units.router)
router.include_router(application_methods.router)
router.include_router(infestation_degrees.router)
router.include_router(cleaning.router)
router.include_router(plague_categories.router)
router.include_router(plagues.router)
router.include_router(cancellation_reasons.router)
router.include_router(origin_sources.router)
router.include_router(service_types.router)
router.include_router(discounts.router)
router.include_router(extras.router)
router.include_router(indications.router)
router.include_router(custom_descriptions.router)
router.include_router(rejection_reasons.router)
router.include_router(price_lists.router)
router.include_router(suppliers.router)
router.include_router(status_router.router)
router.include_router(quotes.router)
