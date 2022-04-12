from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import get_db
from repository import presentation
from schemas.presentation import PresentationRequest, PresentationUpdateRequest, PresentationResponse

router = APIRouter(
    prefix='/presentations',
    tags=['🧰 Presentaciones']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[PresentationResponse])
async def index(db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return presentation.get_all(db, authorize)


@router.get('/{presentation_id}', status_code=status.HTTP_200_OK, response_model=PresentationResponse)
async def show(presentation_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return presentation.retrieve(db, presentation_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=PresentationResponse)
async def store(request: PresentationRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return presentation.create(db, request, authorize)


@router.put('/{presentation_id}', status_code=status.HTTP_202_ACCEPTED, response_model=PresentationResponse)
async def update(presentation_id: UUID4, request: PresentationUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return presentation.update(db, request, presentation_id)


@router.delete('/{presentation_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(presentation_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return presentation.delete(db, presentation_id)
