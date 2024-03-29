from fastapi import APIRouter, Depends, status, Query
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import job_title
from schemas.job_title import JobTitleRequest, JobTitleUpdateRequest, JobTitleResponse

router = APIRouter(
    prefix='/job_titles',
    tags=['📜 Puestos']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[JobTitleResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return job_title.get_all(db, authorize, paginate)


@router.get('/{job_title_id}', status_code=status.HTTP_200_OK, response_model=JobTitleResponse)
async def show(job_title_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return job_title.retrieve(db, job_title_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=JobTitleResponse)
async def store(request: JobTitleRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return job_title.create(db, request, authorize)


@router.put('/{job_title_id}', status_code=status.HTTP_202_ACCEPTED, response_model=JobTitleResponse)
async def update(job_title_id: UUID4, request: JobTitleUpdateRequest, db: Session = Depends(get_db),
                 authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return job_title.update(db, request, job_title_id)


@router.delete('/{job_title_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(job_title_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return job_title.delete(db, job_title_id)
