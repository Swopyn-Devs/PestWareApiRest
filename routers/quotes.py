from fastapi import APIRouter, Depends, status, Query
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import quote
from repository import quote_plague
from schemas.quote import QuoteRequest, QuoteUpdateRequest, QuoteResponse
from schemas.quote_plague import QuotePlagueRequest, QuotePlagueResponse

router = APIRouter(
    prefix='/quotes',
    tags=['📃 Cotizaciones']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[QuoteResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote.get_all(db, authorize, paginate)


@router.get('/{quote_id}/plagues', status_code=status.HTTP_200_OK, response_model=Page[QuotePlagueResponse])
async def index_plague(quote_id: UUID4, paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote_plague.get_all(db, authorize, paginate, quote_id)


@router.get('/{quote_id}', status_code=status.HTTP_200_OK, response_model=QuoteResponse)
async def show(quote_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote.retrieve(db, quote_id)


@router.get('/plagues/{quote_plague_id}', status_code=status.HTTP_200_OK, response_model=QuotePlagueResponse)
async def show_plague(quote_plague_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote_plague.retrieve(db, quote_plague_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=QuoteResponse)
async def store(request: QuoteRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote.create(db, request, authorize)


@router.post('/{quote_id}/plagues', status_code=status.HTTP_201_CREATED, response_model=QuotePlagueResponse)
async def store_plague(quote_id: UUID4, request: QuotePlagueRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote_plague.create(db, request, quote_id)


@router.put('/{quote_id}', status_code=status.HTTP_202_ACCEPTED, response_model=QuoteResponse)
async def update(quote_id: UUID4, request: QuoteUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote.update(db, request, quote_id)


@router.delete('/{quote_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(quote_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote.delete(db, quote_id)


@router.delete('/plagues/{quote_plague_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy_plague(quote_plague_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote_plague.delete(db, quote_plague_id)
