from fastapi import APIRouter, Depends, status, Query
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import quote
from repository import quote_plague
from repository import quote_concept
from repository import quote_extra
from schemas.quote import QuoteApproveRequest, QuoteRejectRequest, QuoteRequest, QuoteUpdateRequest, QuoteResponse
from schemas.quoter import QuoterRequest, QuoterResponse
from schemas.quote_plague import QuotePlagueRequest, QuotePlagueResponse
from schemas.quote_concept import QuoteConceptRequest, QuoteConceptResponse
from schemas.quote_extra import QuoteExtraRequest, QuoteExtraResponse

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


@router.get('/{quote_id}/concepts', status_code=status.HTTP_200_OK, response_model=Page[QuoteConceptResponse])
async def index_concept(quote_id: UUID4, paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote_concept.get_all(db, authorize, paginate, quote_id)


@router.get('/{quote_id}/extras', status_code=status.HTTP_200_OK, response_model=Page[QuoteExtraResponse])
async def index_extra(quote_id: UUID4, paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote_extra.get_all(db, authorize, paginate, quote_id)


@router.get('/{quote_id}', status_code=status.HTTP_200_OK, response_model=QuoteResponse)
async def show(quote_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote.retrieve(db, quote_id)


@router.get('/plagues/{quote_plague_id}', status_code=status.HTTP_200_OK, response_model=QuotePlagueResponse)
async def show_plague(quote_plague_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote_plague.retrieve(db, quote_plague_id)


@router.get('/concepts/{quote_concept_id}', status_code=status.HTTP_200_OK, response_model=QuoteConceptResponse)
async def show_concept(quote_concept_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote_concept.retrieve(db, quote_concept_id)


@router.get('/extras/{quote_extra_id}', status_code=status.HTTP_200_OK, response_model=QuoteExtraResponse)
async def show_extra(quote_extra_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote_extra.retrieve(db, quote_extra_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=QuoteResponse)
async def store(request: QuoteRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote.create(db, request, authorize)


@router.post('/{quote_id}/plagues', status_code=status.HTTP_201_CREATED, response_model=QuotePlagueResponse)
async def store_plague(quote_id: UUID4, request: QuotePlagueRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote_plague.create(db, request, quote_id)


@router.post('/{quote_id}/concepts', status_code=status.HTTP_201_CREATED, response_model=QuoteConceptResponse)
async def store_concept(quote_id: UUID4, request: QuoteConceptRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote_concept.create(db, request, quote_id)


@router.post('/{quote_id}/extras', status_code=status.HTTP_201_CREATED, response_model=QuoteExtraResponse)
async def store_extra(quote_id: UUID4, request: QuoteExtraRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote_extra.create(db, request, quote_id)


@router.put('/{quote_id}', status_code=status.HTTP_202_ACCEPTED, response_model=QuoteResponse)
async def update(quote_id: UUID4, request: QuoteUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote.update(db, request, quote_id)


@router.patch('/{quote_id}/approve', status_code=status.HTTP_202_ACCEPTED, response_model=QuoteResponse)
async def approve(quote_id: UUID4, request: QuoteApproveRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote.approve(db, request, quote_id)


@router.patch('/{quote_id}/reject', status_code=status.HTTP_202_ACCEPTED, response_model=QuoteResponse)
async def reject(quote_id: UUID4, request: QuoteRejectRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote.reject(db, request, quote_id)


@router.put('/plagues/{quote_plague_id}', status_code=status.HTTP_202_ACCEPTED, response_model=QuotePlagueResponse)
async def update_plague(quote_plague_id: UUID4, request: QuotePlagueRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote_plague.update(db, request, quote_plague_id)


@router.put('/concepts/{quote_concept_id}', status_code=status.HTTP_202_ACCEPTED, response_model=QuoteConceptResponse)
async def update_concept(quote_concept_id: UUID4, request: QuoteConceptRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote_concept.update(db, request, quote_concept_id)


@router.put('/extras/{quote_extra_id}', status_code=status.HTTP_202_ACCEPTED, response_model=QuoteExtraResponse)
async def update_extra(quote_extra_id: UUID4, request: QuoteExtraRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote_extra.update(db, request, quote_extra_id)


@router.delete('/{quote_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(quote_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote.delete(db, quote_id)


@router.delete('/plagues/{quote_plague_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy_plague(quote_plague_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote_plague.delete(db, quote_plague_id)


@router.delete('/concepts/{quote_concept_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy_concept(quote_concept_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote_concept.delete(db, quote_concept_id)


@router.delete('/extras/{quote_extra_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy_extra(quote_extra_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote_extra.delete(db, quote_extra_id)


@router.post('/quoter', status_code=status.HTTP_200_OK, response_model=QuoterResponse)
async def quoter(request: QuoterRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return quote.quoter(db, authorize, request)
