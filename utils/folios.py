from fastapi import HTTPException, status
from models.customer import Customer
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
