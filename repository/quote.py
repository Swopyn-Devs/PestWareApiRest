from models.tax import Tax
from utils.functions import *
from utils import folios

from pydantic import UUID4
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
from fastapi import HTTPException, status

from models.quote import Quote
from models.service_type import ServiceType
from models.customer import Customer
from models.origin_source import OriginSource
from models.discount import Discount
from models.employee import Employee
from models.price_list import PriceList
from models.job_center import JobCenter
from models.rejection_reason import RejectionReason
from schemas.quote import QuoteApproveRequest, QuoteRejectRequest, QuoteRequest, QuoteUpdateRequest
from schemas.quoter import QuoterRequest, QuoterResponse

model_name = 'cotización'


def get_all(db: Session, authorize: AuthJWT, paginate_param: bool):
    return get_all_data(db, Quote, authorize, paginate_param, True)


def retrieve(db: Session, model_id: UUID4):
    return get_data(db, Quote, model_id, model_name)


def create(db: Session, request: QuoteRequest, authorize: AuthJWT):
    employee = get_employee_id_by_token(db, authorize)
    get_data(db, ServiceType, request.service_type_id, 'tipo de servicio')
    get_data(db, Customer, request.customer_id, 'cliente')
    get_data(db, Employee, request.employee_id, 'empleado')

    origin_source_id = None
    discount_id = None
    price_list_id = None

    if request.origin_source_id is not None:
        get_data(db, OriginSource, request.origin_source_id, 'fuente de origen')
        origin_source_id = request.origin_source_id
    if request.discount_id is not None:
        get_data(db, Discount, request.discount_id, 'descuento')
        discount_id = request.discount_id
    if request.price_list_id is not None:
        get_data(db, PriceList, request.price_list_id, 'lista de precio')
        price_list_id = request.price_list_id

    folio = folios.quote(db, employee.job_center_id)
    request_data = Quote(
        folio=folio,
        quantity=request.quantity,
        subtotal=request.subtotal,
        total=request.total,
        tax=request.tax,
        sent_mail=request.sent_mail,
        sent_whatsapp=request.sent_whatsapp,
        approved=request.approved,
        service_type_id=request.service_type_id,
        customer_id=request.customer_id,
        origin_source_id=origin_source_id,
        discount_id=discount_id,
        employee_id=request.employee_id,
        price_list_id=price_list_id,
        status_id=get_status_id(),
        job_center_id=employee.job_center_id
    )
    last_id = insert_data(db, request_data)
    return get_data(db, Quote, last_id, model_name)


def update(db: Session, request: QuoteUpdateRequest, model_id: UUID4):
    get_data(db, ServiceType, request.service_type_id, 'tipo de servicio')
    get_data(db, Customer, request.customer_id, 'cliente')
    get_data(db, Employee, request.employee_id, 'empleado')
    get_data(db, JobCenter, request.job_center_id, 'centro de trabajo')

    if request.origin_source_id is not None:
        get_data(db, OriginSource, request.origin_source_id, 'fuente de origen')
    if request.discount_id is not None:
        get_data(db, Discount, request.discount_id, 'descuento')
    if request.price_list_id is not None:
        get_data(db, PriceList, request.price_list_id, 'lista de precio')

    return update_data(db, Quote, model_id, model_name, request.dict())


def delete(db: Session, model_id: UUID4):
    return update_delete(db, Quote, model_id, model_name)


def approve(db: Session, request: QuoteApproveRequest, model_id: UUID4):
    return update_data(db, Quote, model_id, model_name, request.dict())


def reject(db: Session, request: QuoteRejectRequest, model_id: UUID4):
    get_data(db, RejectionReason, request.rejection_reason_id, 'motivo de rechazo')
    return update_data(db, Quote, model_id, model_name, request.dict())


def quoter(db: Session, authorize: AuthJWT, request: QuoterRequest):
    employee = get_employee_id_by_token(db, authorize)
    price_lists = db.query(PriceList).filter(PriceList.service_type_id == request.service_type_id)
    if price_lists.count() == 0:
        return QuoterResponse(
            price_list=None,
            subtotal=0,
            extras=0,
            discount=0,
            tax=0,
            total=0
        )

    price_list_with_higher_hierarchy: PriceList = None
    for price_list in price_lists.all():
        if price_list_with_higher_hierarchy is None:
            price_list_with_higher_hierarchy = price_list
        elif price_list.hierarchy > price_list_with_higher_hierarchy.hierarchy:
            price_list_with_higher_hierarchy = price_list

    subtotal = 0
    tax = 0
    discount = 0
    extras = 0
    total = 0

    subtotal = float(price_list_with_higher_hierarchy.cost) * request.quantity

    if subtotal < price_list_with_higher_hierarchy.min_cost:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f'El costo no puede ser menor a {price_list_with_higher_hierarchy.min_cost}.')

    if request.extras_quote:
        if len(request.extras_quote) > 0:
            for extra_quote in request.extras_quote:
                extra = db.query(Extra).filter(Extra.id == extra_quote.extra_id).first()
                extras = extras + (extra.quantity * extra_quote.quantity)


    if request.discount_id:
        if request.discount_id is not None:
            discount_db = db.query(Discount).filter(Discount.id == request.discount_id).first()
            discount_db = discount_db.percentage / 100
            discount = subtotal * discount_db


    if request.is_tax:
        tax_main = db.query(Tax).filter(Tax.is_main == True).filter(Tax.job_center_id == employee.job_center_id).first()
        if not tax_main:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Debes configurar un impuesto principal en el catalogo de impuestos.')
        tax_main = tax_main.value / 100
        tax = ((subtotal + extras) - discount) * tax_main

    total = (subtotal + tax + extras) - discount

    return QuoterResponse(
        price_list=price_list_with_higher_hierarchy.id,
        subtotal=subtotal,
        extras=extras,
        discount=discount,
        tax=tax,
        total=total
    )
