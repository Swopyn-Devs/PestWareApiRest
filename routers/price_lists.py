from fastapi import APIRouter, Depends, status, Query, UploadFile
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import price_list
from repository import price_list_price
from repository import price_list_plague
from schemas.price_list import PriceListRequest, PriceListResponse
from schemas.price_list_price import PriceListPriceRequest, PriceListPriceUpdateRequest, PriceListPriceResponse
from schemas.price_list_plague import PriceListPlagueRequest, PriceListPlagueResponse

router = APIRouter(
    prefix='/price-lists',
    tags=['📋 Lista de precios']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[PriceListResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return price_list.get_all(db, authorize, paginate)


@router.get('/{price_list_id}/prices', status_code=status.HTTP_200_OK, response_model=Page[PriceListPriceResponse])
async def index_price(price_list_id: UUID4, paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return price_list_price.get_all(db, authorize, paginate, price_list_id)


@router.get('/{price_list_id}/plagues', status_code=status.HTTP_200_OK, response_model=Page[PriceListPlagueResponse])
async def index_plague(price_list_id: UUID4, paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return price_list_plague.get_all(db, authorize, paginate, price_list_id)


@router.get('/{price_list_id}', status_code=status.HTTP_200_OK, response_model=PriceListResponse)
async def show(price_list_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return price_list.retrieve(db, price_list_id)


@router.get('/prices/{price_list_price_id}', status_code=status.HTTP_200_OK, response_model=PriceListPriceResponse)
async def show_price(price_list_price_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return price_list_price.retrieve(db, price_list_price_id)


@router.get('/plagues/{price_list_plague_id}', status_code=status.HTTP_200_OK, response_model=PriceListPlagueResponse)
async def show_plague(price_list_plague_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return price_list_plague.retrieve(db, price_list_plague_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=PriceListResponse)
async def store(request: PriceListRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return price_list.create(db, request, authorize)


@router.post('/{price_list_id}/prices', status_code=status.HTTP_201_CREATED, response_model=PriceListPriceResponse)
async def store_price(price_list_id: UUID4, request: PriceListPriceRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return price_list_price.create(db, request, price_list_id)


@router.post('/{price_list_id}/plagues', status_code=status.HTTP_201_CREATED, response_model=PriceListPlagueResponse)
async def store_plague(price_list_id: UUID4, request: PriceListPlagueRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return price_list_plague.create(db, request, price_list_id)


@router.put('/{price_list_id}', status_code=status.HTTP_202_ACCEPTED, response_model=PriceListResponse)
async def update(price_list_id: UUID4, request: PriceListRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return price_list.update(db, request, price_list_id)


@router.put('/prices/{price_list_price_id}', status_code=status.HTTP_202_ACCEPTED, response_model=PriceListPriceResponse)
async def update_price(price_list_price_id: UUID4, request: PriceListPriceUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return price_list_price.update(db, request, price_list_price_id)


@router.patch('/{price_list_id}/cover', status_code=status.HTTP_202_ACCEPTED, response_model=PriceListResponse)
async def update_cover(price_list_id: UUID4, file: UploadFile, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return price_list.update_cover(db, file, price_list_id, authorize)


@router.delete('/{price_list_id}/cover', status_code=status.HTTP_202_ACCEPTED, response_model=PriceListResponse)
async def delete_cover(price_list_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return price_list.delete_cover(db, price_list_id)


@router.delete('/{price_list_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(price_list_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return price_list.delete(db, price_list_id)


@router.delete('/prices/{price_list_price_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy_price(price_list_price_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return price_list_price.delete(db, price_list_price_id)


@router.delete('/plagues/{price_list_plague_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy_plague(price_list_plague_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return price_list_plague.delete(db, price_list_plague_id)
