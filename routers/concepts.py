from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import get_db
from repository import concept
from schemas.concept import ConceptRequest, ConceptUpdateRequest, ConceptResponse

router = APIRouter(
    prefix='/concepts',
    tags=['📦️ Conceptos']
)


@router.get('/{paginate}', status_code=status.HTTP_200_OK, response_model=Page[ConceptResponse])
async def index(paginate: bool, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return concept.get_all(db, authorize, paginate)


@router.get('/{concept_id}', status_code=status.HTTP_200_OK, response_model=ConceptResponse)
async def show(concept_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return concept.retrieve(db, concept_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=ConceptResponse)
async def store(request: ConceptRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return concept.create(db, request, authorize)


@router.put('/{concept_id}', status_code=status.HTTP_202_ACCEPTED, response_model=ConceptResponse)
async def update(concept_id: UUID4, request: ConceptUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return concept.update(db, request, concept_id)


@router.delete('/{concept_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(concept_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return concept.delete(db, concept_id)
