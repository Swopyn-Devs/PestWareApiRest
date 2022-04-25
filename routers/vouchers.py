from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import get_db
from repository import voucher
from schemas.voucher import VoucherRequest, VoucherUpdateRequest, VoucherResponse

router = APIRouter(
    prefix='/vouchers',
    tags=['📄 Comprobantes']
)


@router.get('/{paginate}', status_code=status.HTTP_200_OK, response_model=Page[VoucherResponse])
async def index(paginate: bool, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return voucher.get_all(db, authorize, paginate)


@router.get('/{voucher_id}', status_code=status.HTTP_200_OK, response_model=VoucherResponse)
async def show(voucher_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return voucher.retrieve(db, voucher_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=VoucherResponse)
async def store(request: VoucherRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return voucher.create(db, request, authorize)


@router.put('/{voucher_id}', status_code=status.HTTP_202_ACCEPTED, response_model=VoucherResponse)
async def update(voucher_id: UUID4, request: VoucherUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return voucher.update(db, request, voucher_id)


@router.delete('/{voucher_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(voucher_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return voucher.delete(db, voucher_id)
