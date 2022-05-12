from fastapi import APIRouter, Depends, status, Query
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import supplier
from schemas.supplier import SupplierRequest, SupplierUpdateRequest, SupplierResponse

router = APIRouter(
    prefix='/suppliers',
    tags=['🚚 Proveedores']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[SupplierResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return supplier.get_all(db, authorize, paginate)


@router.get('/{supplier_id}', status_code=status.HTTP_200_OK, response_model=SupplierResponse)
async def show(supplier_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return supplier.retrieve(db, supplier_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=SupplierResponse)
async def store(request: SupplierRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return supplier.create(db, request, authorize)


@router.put('/{supplier_id}', status_code=status.HTTP_202_ACCEPTED, response_model=SupplierResponse)
async def update(supplier_id: UUID4, request: SupplierUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return supplier.update(db, request, supplier_id)


@router.delete('/{supplier_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(supplier_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return supplier.delete(db, supplier_id)
