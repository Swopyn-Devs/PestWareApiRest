from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import get_db
from repository import infestation_degree
from schemas.infestation_degree import InfestationDegreeRequest, InfestationDegreeUpdateRequest, InfestationDegreeResponse

router = APIRouter(
    prefix='/infestation-degrees',
    tags=['📏 Grados de infestación']
)


@router.get('/{paginate}', status_code=status.HTTP_200_OK, response_model=Page[InfestationDegreeResponse])
async def index(paginate: bool, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return infestation_degree.get_all(db, authorize, paginate)


@router.get('/{infestation_degree_id}', status_code=status.HTTP_200_OK, response_model=InfestationDegreeResponse)
async def show(infestation_degree_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return infestation_degree.retrieve(db, infestation_degree_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=InfestationDegreeResponse)
async def store(request: InfestationDegreeRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return infestation_degree.create(db, request, authorize)


@router.put('/{infestation_degree_id}', status_code=status.HTTP_202_ACCEPTED, response_model=InfestationDegreeResponse)
async def update(infestation_degree_id: UUID4, request: InfestationDegreeUpdateRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return infestation_degree.update(db, request, infestation_degree_id)


@router.delete('/{infestation_degree_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(infestation_degree_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return infestation_degree.delete(db, infestation_degree_id)
