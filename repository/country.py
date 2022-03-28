from fastapi import HTTPException, status
from pydantic import UUID4
from sqlalchemy.orm import Session

from models.catalog import Country
from schemas.catalog import CountryRequest


def get_all(db: Session):
    return db.query(Country).all()


def retrieve(db: Session, country_id: UUID4):
    country = db.query(Country).filter(Country.id == country_id).first()
    if not country:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El país con el id {country_id} no esta disponible.')
    return country


def create(db: Session, request: CountryRequest):
    new_country = Country(
        name=request.name,
        code_country=request.code_country,
        coin_country=request.coin_country,
        symbol_country=request.symbol_country
    )
    db.add(new_country)
    db.commit()
    db.refresh(new_country)
    return new_country


def update(db: Session, request: CountryRequest, country_id: UUID4):
    country = db.query(Country).filter(Country.id == country_id)
    if not country.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El país con el id {country_id} no esta disponible.')
    country.update(request.dict())
    db.commit()
    return country.first()


def destroy(db: Session, country_id: UUID4):
    country = db.query(Country).filter(Country.id == country_id)
    if not country.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El país con el id {country_id} no esta disponible.')

    country.delete(synchronize_session=False)
    db.commit()
    return {'message': 'Country delete successful.'}
