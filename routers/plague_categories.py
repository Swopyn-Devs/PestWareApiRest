from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import get_db
from repository import plague_category
from schemas.plague_category import PlagueCategoryRequest, PlagueCategoryUpdateRequest, PlagueCategoryResponse

router = APIRouter(
    prefix='/plague-categories',
    tags=['🗃️ Categorías de plagas']
)


@router.get('/{paginate}', status_code=status.HTTP_200_OK, response_model=Page[PlagueCategoryResponse])
async def index(paginate: bool, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return plague_category.get_all(db, authorize, paginate)


@router.get('/{plague_category_id}', status_code=status.HTTP_200_OK, response_model=PlagueCategoryResponse)
async def show(plague_category_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return plague_category.retrieve(db, plague_category_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=PlagueCategoryResponse)
async def store(request: PlagueCategoryRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return plague_category.create(db, request, authorize)


@router.put('/{plague_category_id}', status_code=status.HTTP_202_ACCEPTED, response_model=PlagueCategoryResponse)
async def update(plague_category_id: UUID4, request: PlagueCategoryUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return plague_category.update(db, request, plague_category_id)


@router.delete('/{plague_category_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(plague_category_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return plague_category.delete(db, plague_category_id)
