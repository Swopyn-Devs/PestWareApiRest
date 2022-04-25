from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import get_db
from repository import cleaning
from schemas.cleaning import CleaningRequest, CleaningUpdateRequest, CleaningResponse

router = APIRouter(
    prefix='/cleaning',
    tags=['🗑️ Orden y limpieza']
)


@router.get('/{paginate}', status_code=status.HTTP_200_OK, response_model=Page[CleaningResponse])
async def index(paginate: bool, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return cleaning.get_all(db, authorize, paginate)


@router.get('/{cleaning_id}', status_code=status.HTTP_200_OK, response_model=CleaningResponse)
async def show(cleaning_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return cleaning.retrieve(db, cleaning_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=CleaningResponse)
async def store(request: CleaningRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return cleaning.create(db, request, authorize)


@router.put('/{cleaning_id}', status_code=status.HTTP_202_ACCEPTED, response_model=CleaningResponse)
async def update(cleaning_id: UUID4, request: CleaningUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return cleaning.update(db, request, cleaning_id)


@router.delete('/{cleaning_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(cleaning_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return cleaning.delete(db, cleaning_id)
