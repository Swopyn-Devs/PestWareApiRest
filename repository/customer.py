from fastapi import HTTPException, status
from fastapi_pagination import paginate
from fastapi_jwt_auth import AuthJWT
from pydantic import UUID4
from sqlalchemy.orm import Session

from models.customer import Customer
from schemas.customer import CustomerRequest, CustomerRequestUpdated, CustomerResponse
from utils import folios, functions


def get_all(db: Session, authorize: AuthJWT, main_customer):
    employee = functions.get_employee_id_by_token(db, authorize)
    data = []
    customers = db.query(Customer).filter(Customer.job_center_id == employee.job_center_id).filter(Customer.is_deleted == False)
    if main_customer is not None:
        customers = customers.filter(Customer.main_customer_id == main_customer)

    for customer in customers.all():
        data.append(response_customer(db, customer))
    return paginate(data)


def retrieve(db: Session, customer_id: UUID4):
    customer = db.query(Customer).filter(Customer.id == customer_id).filter(Customer.is_deleted == False).first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El cliente con el id {customer_id} no esta disponible.')

    return response_customer(db, customer)


def create(db: Session, request: CustomerRequest):
    folio = folios.customer(db, request.job_center_id, request.main_customer_id, request.is_main)

    new_customer = Customer(
        name=request.name,
        folio=folio,
        phone=request.phone,
        email=request.email,
        contact_name=request.contact_name,
        contact_phone=request.contact_phone,
        contact_email=request.contact_email,
        address=request.address,
        is_main=request.is_main,
        main_customer_id=request.main_customer_id,
        job_center_id=request.job_center_id,
        is_active=True
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return response_customer(db, new_customer)


def update(db: Session, request: CustomerRequestUpdated, customer_id: UUID4):
    customer = db.query(Customer).filter(Customer.id == customer_id).filter(Customer.is_deleted == False)
    if not customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El cliente con el id {customer_id} no esta disponible.')

    customer.update(request.dict())
    db.commit()

    return response_customer(db, customer.first())


def delete(db: Session, customer_id: UUID4):
    customer = db.query(Customer).filter(Customer.id == customer_id)
    if not customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El cliente con el id {customer_id} no esta disponible.')

    customer.update({'is_deleted': True})
    db.commit()

    return {'detail': 'El cliente se elimino correctamente.'}


def get_total_branches(db: Session, customer_id: UUID4):
    return db.query(Customer).filter(Customer.main_customer_id == customer_id).filter(Customer.is_deleted == False).count()


def response_customer(db, customer):
    return CustomerResponse(
        id=customer.id,
        name=customer.name,
        folio=customer.folio,
        phone=customer.phone,
        email=customer.email,
        contact_name=customer.contact_name,
        contact_phone=customer.contact_phone,
        contact_email=customer.contact_email,
        address=customer.address,
        is_main=customer.is_main,
        main_customer_id=customer.main_customer_id,
        job_center_id=customer.job_center_id,
        total_branches=get_total_branches(db, customer.id),
        total_quotes=23,
        total_scheduled_services=68,
        total_completed_services=140,
        total_canceled_services=4,
        quotes_balance=167421.28,
        scheduled_services_balance=83026.00,
        collected_balance=217021.00,
        past_due_balance=4000.13,
        is_active=customer.is_active,
        created_at=customer.created_at,
        updated_at=customer.updated_at
    )
