from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import get_db
from repository import tax
from schemas.tax import TaxRequest, TaxResponse

router = APIRouter(
    prefix='/taxes',
    tags=['💰 Impuestos']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[TaxResponse])
async def index(db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return tax.get_all(db)


@router.get('/{tax_id}', status_code=status.HTTP_200_OK, response_model=TaxResponse)
async def show(tax_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return tax.retrieve(db, tax_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=TaxResponse)
async def store(request: TaxRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return tax.create(db, request)


@router.put('/{tax_id}', status_code=status.HTTP_202_ACCEPTED, response_model=TaxResponse)
async def update(tax_id: UUID4, request: TaxRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return tax.update(db, request, tax_id)


@router.delete('/{tax_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(tax_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return tax.delete(db, tax_id)
