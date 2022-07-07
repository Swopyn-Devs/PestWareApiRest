from utils.functions import *

from fastapi import HTTPException, status
from fastapi_pagination import paginate
from fastapi_jwt_auth import AuthJWT
from pydantic import UUID4
from sqlalchemy.orm import Session

from models.job_center import JobCenter
from models.customer import Customer
from models.business_activity import BusinessActivity
from schemas.customer import CustomerRequest, CustomerRequestUpdated, CustomerResponse, CustomerXlsxResponse
import repository.job_center as job_center_repo
from utils import folios, functions
from fakers import customer as customer_faker


model_name = 'cliente'


def get_all(db: Session, authorize: AuthJWT, is_main, main_customer, folio, name, is_active, contact):
    employee = functions.get_employee_id_by_token(db, authorize)
    data = []
    customers = db.query(Customer).filter(Customer.job_center_id == employee.job_center_id).filter(Customer.is_deleted == False)
    if is_main is not None:
        customers = customers.filter(Customer.is_main == is_main)
    if main_customer is not None:
        customers = customers.filter(Customer.main_customer_id == main_customer)
    if folio is not None:
        customers = customers.filter(Customer.folio == folio)
    if name is not None:
        search = "%{}%".format(name)
        customers = customers.filter(Customer.name.like(search))
    if is_active is not None:
        customers = customers.filter(Customer.is_active == is_active)
    if contact is not None:
        search = "%{}%".format(contact)
        customers = customers.filter(Customer.contact_name.like(search))

    for customer in customers.all():
        data.append(response_customer(db, customer))

    return paginate(data)


def retrieve(db: Session, customer_id: UUID4):
    data = functions.get_data(db, Customer, customer_id, model_name)
    return response_customer(db, data)


def create(db: Session, request: CustomerRequest):
    functions.get_data(db, BusinessActivity, request.business_activity_id, 'giro de la empresa')
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
        address_latitude=request.address_latitude,
        address_longitude=request.address_longitude,
        is_main=request.is_main,
        main_customer_id=request.main_customer_id,
        business_activity_id=request.business_activity_id,
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


def csv(db: Session, model_id: UUID4):
    customer_data = functions.get_data(db, Customer, model_id, model_name)
    test_data = db.query(Customer).all()
    print(test_data)
    csv_data = functions.create_csv(test_data)
    return csv_data


def faker(db: Session, count: int):
    customer_faker.create(db, count)

    return {'detail': 'Clientes generados correctamente.'}


def get_total_branches(db: Session, customer_id: UUID4):
    return db.query(Customer).filter(Customer.main_customer_id == customer_id).filter(Customer.is_deleted == False).count()


def response_customer(db, customer):
    if type(customer) is dict:
        if customer['email'] == 'None':
            customer['email'] = None
        if customer['main_customer_id'] == 'None':
            customer['main_customer_id'] = None
        if customer['address_latitude'] == 'None':
            customer['address_latitude'] = None
        if customer['address_longitude'] == 'None':
            customer['address_longitude'] = None

        return CustomerResponse(
            id=customer['id'],
            name=customer['name'],
            folio=customer['folio'],
            phone=customer['phone'],
            email=customer['email'],
            contact_name=customer['contact_name'],
            contact_phone=customer['contact_phone'],
            contact_email=customer['contact_email'],
            address=customer['address'],
            address_latitude=customer['address_latitude'],
            address_longitude=customer['address_longitude'],
            is_main=customer['is_main'],
            main_customer_id=customer['main_customer_id'],
            job_center_id=customer['job_center_id'],
            business_activity_id=customer['business_activity_id'],
            total_branches=get_total_branches(db, customer['id']),
            total_quotes=23,
            total_scheduled_services=68,
            total_completed_services=140,
            total_canceled_services=4,
            quotes_balance=167421.28,
            scheduled_services_balance=83026.00,
            collected_balance=217021.00,
            past_due_balance=4000.13,
            is_active=customer['is_active'],
            created_at=customer['created_at'],
            updated_at=customer['updated_at']
        )
    else:
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
            address_latitude=customer.address_latitude,
            address_longitude=customer.address_longitude,
            is_main=customer.is_main,
            main_customer_id=customer.main_customer_id,
            job_center_id=functions.get_data(db, JobCenter, customer.job_center_id, 'centro de trabajo'),
            business_activity_id=functions.get_data(db, BusinessActivity, customer.business_activity_id, 'giro de la empresa'),
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
