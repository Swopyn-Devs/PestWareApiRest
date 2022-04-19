from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import get_db
from repository import discount
from schemas.discount import DiscountRequest, DiscountUpdateRequest, DiscountResponse

router = APIRouter(
    prefix='/discounts',
    tags=['💸 Descuentos']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[DiscountResponse])
async def index(db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return discount.get_all(db, authorize)


@router.get('/{discount_id}', status_code=status.HTTP_200_OK, response_model=DiscountResponse)
async def show(discount_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return discount.retrieve(db, discount_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=DiscountResponse)
async def store(request: DiscountRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return discount.create(db, request, authorize)


@router.put('/{discount_id}', status_code=status.HTTP_202_ACCEPTED, response_model=DiscountResponse)
async def update(discount_id: UUID4, request: DiscountUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return discount.update(db, request, discount_id)


@router.delete('/{discount_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(discount_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return discount.delete(db, discount_id)
