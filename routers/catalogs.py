from typing import List

from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import get_db
from documentation.catalogs import *
from repository import country
from schemas.catalog import CountryResponse, CountryRequest

router = APIRouter(
    prefix='/catalogs/countries',
    tags=['🇲🇽 Países']
)


@router.get('', response_model=List[CountryResponse], name=name_index, description=desc_index)
async def index(db: Session = Depends(get_db)):
    return country.get_all(db)


@router.get('/{country_id}', status_code=status.HTTP_200_OK, response_model=CountryResponse,
            name=name_show, description=desc_show)
async def show(country_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return country.retrieve(db, country_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=CountryResponse,
             name=name_store, description=desc_store)
async def store(request: CountryRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return country.create(db, request)


@router.put('/{country_id}', status_code=status.HTTP_202_ACCEPTED, response_model=CountryResponse,
            name=name_update, description=desc_update)
async def update(country_id: UUID4, request: CountryRequest, db: Session = Depends(get_db),
                 authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return country.update(db, request, country_id)


@router.delete('/{country_id}', status_code=status.HTTP_404_NOT_FOUND, name=name_destroy, description=desc_destroy)
async def destroy(country_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return country.destroy(db, country_id)
