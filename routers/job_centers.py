from fastapi import APIRouter, Depends, status, UploadFile, Query
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from repository import job_center
from schemas.job_center import JobCenterRequest, JobCenterResponse

router = APIRouter(
    prefix='/job-centers',
    tags=['🏤 Centros de Trabajo']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[JobCenterResponse])
async def index(paginate: Optional[bool] = Query(None), db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return job_center.get_all(db, authorize, paginate)


@router.get('/{job_center_id}', status_code=status.HTTP_200_OK, response_model=JobCenterResponse)
async def show(job_center_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return job_center.retrieve(db, job_center_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=JobCenterResponse)
async def store(request: JobCenterRequest, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return job_center.create(db, request)


@router.put('/{job_center_id}', status_code=status.HTTP_202_ACCEPTED, response_model=JobCenterResponse)
async def update(job_center_id: UUID4, request: JobCenterRequest, db: Session = Depends(get_db),
                 authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return job_center.update(db, request, job_center_id)


@router.patch('/{job_center_id}/sanitary_license', status_code=status.HTTP_202_ACCEPTED,
              response_model=JobCenterResponse)
async def update_sanitary_license(job_center_id: UUID4, file: UploadFile, db: Session = Depends(get_db),
                                  authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return job_center.update_sanitary_license(db, file, job_center_id)


@router.delete('/{job_center_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(job_center_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return job_center.delete(db, job_center_id)
