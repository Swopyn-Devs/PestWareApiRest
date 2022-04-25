from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import get_db
from repository import plague
from schemas.plague import PlagueRequest, PlagueUpdateRequest, PlagueResponse

router = APIRouter(
    prefix='/plagues',
    tags=['🐜 Plagas']
)


@router.get('/{paginate}', status_code=status.HTTP_200_OK, response_model=Page[PlagueResponse])
async def index(paginate: bool,db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return plague.get_all(db, authorize, paginate)


@router.get('/{plague_id}', status_code=status.HTTP_200_OK, response_model=PlagueResponse)
async def show(plague_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return plague.retrieve(db, plague_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=PlagueResponse)
async def store(request: PlagueRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return plague.create(db, request, authorize)


@router.put('/{plague_id}', status_code=status.HTTP_202_ACCEPTED, response_model=PlagueResponse)
async def update(plague_id: UUID4, request: PlagueUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return plague.update(db, request, plague_id)


@router.delete('/{plague_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(plague_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return plague.delete(db, plague_id)
