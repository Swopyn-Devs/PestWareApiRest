from faker import Faker
from repository import customer
from schemas.customer import CustomerRequest
from sqlalchemy.orm import Session
from utils import folios


customer_fake = Faker('es_MX')
Faker.seed(0)
customer_fake.seed_instance(0)

def create(db: Session, count: int):
    for _ in range(count):
        job_center_id = 'be26be0d-d3e0-476d-b506-b2bdbdb3f116'
        business_activity_id = '90821ce9-b1c1-4510-9cc6-a29ed7b4a34d'
        folio = folios.customer(db, job_center_id, False, True)
        fake = CustomerRequest(
            name=customer_fake.company(),
            folio=folio,
            phone=customer_fake.phone_number(),
            email=customer_fake.email(),
            contact_name=customer_fake.unique.name(),
            contact_phone=customer_fake.phone_number(),
            contact_email=customer_fake.email(),
            address=customer_fake.address(),
            is_main=True,
            business_activity_id=business_activity_id,
            job_center_id=job_center_id,
            is_active=True
        )
        customer.create(db, fake)
        print(fake.name)
