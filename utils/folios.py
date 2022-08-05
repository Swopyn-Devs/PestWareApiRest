from fastapi import HTTPException, status
from models.customer import Customer
from models.quote import Quote
from models.event import Event
from models.event_type import EventType
from pydantic import UUID4


def customer(db, job_center_id: UUID4, main_customer_id, main_customer=True) -> str:
    if main_customer:
        last = db.query(Customer).filter(Customer.job_center_id == job_center_id).filter(Customer.is_main == True) \
            .order_by(Customer.created_at.desc()).first()
        folio = f'CL-1000'
        if last is not None:
            last_folio = int(last.folio.split('-')[1])
            last_folio += 1
            folio = f'CL-{last_folio}'
        return folio
    else:
        customer_main = db.query(Customer).filter(Customer.id == main_customer_id).first()
        if not customer_main:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'El cliente con el id {main_customer_id} no esta disponible.')

        last_branch = db.query(Customer).filter(Customer.main_customer_id == main_customer_id) \
            .order_by(Customer.created_at.desc()).first()
        last_folio_branch = 0
        if last_branch:
            last_folio_branch = int(last_branch.folio.split('-')[2])
        customer_folio = customer_main.folio.split('-')[1]
        last_folio_branch += 1
        folio = f'CL-{customer_folio}-{last_folio_branch}'
        return folio


def quote(db, job_center_id: UUID4) -> str:
    last = db.query(Quote).filter(Quote.job_center_id == job_center_id) \
        .order_by(Quote.created_at.desc()).first()
    folio = f'C-1000'
    if last is not None:
        last_folio = int(last.folio.split('-')[1])
        last_folio += 1
        folio = f'C-{last_folio}'
    return folio


def event(db, job_center_id: UUID4, event_type_id: UUID4) -> str:
    event_type = db.query(EventType).filter(EventType.id == event_type_id).first()
    last = db.query(Event).filter(Event.job_center_id == job_center_id) \
        .order_by(Event.created_at.desc()).first()
    folio = f'{event_type.folio_key_setting}-{event_type.folio_init_setting}'
    if last is not None:
        last_folio = int(last.folio.split('-')[1])
        last_folio += 1
        folio = f'{event_type.folio_key_setting}-{last_folio}'
    return folio
