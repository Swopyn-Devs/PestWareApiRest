from fastapi import HTTPException, status
from fastapi_pagination import paginate
from pydantic import UUID4
from sqlalchemy.orm import Session

from models.job_title import JobTitle
from schemas.job_title import JobTitleRequest


def get_all(db: Session):
    return paginate(db.query(JobTitle).all())


def retrieve(db: Session, job_title_id: UUID4):
    job_title = db.query(JobTitle).filter(JobTitle.id == job_title_id).first()
    if not job_title:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El puesto con el id {job_title_id} no esta disponible.')
    return job_title


def create(db: Session, request: JobTitleRequest):
    new_job_title = JobTitle(
        name=request.name,
        job_center_id=request.job_center_id,
    )
    db.add(new_job_title)
    db.commit()
    db.refresh(new_job_title)

    return new_job_title


def update(db: Session, request: JobTitleRequest, job_title_id: UUID4):
    job_title = db.query(JobTitle).filter(JobTitle.id == job_title_id)
    if not job_title.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El puesto con el id {job_title_id} no está disponible.')

    job_title.update(request.dict())
    db.commit()

    return job_title.first()


def delete(db: Session, job_title_id: UUID4):
    job_title = db.query(JobTitle).filter(JobTitle.id == job_title_id)
    if not job_title.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El puesto con el id {job_title_id} no está disponible.')

    job_title.update({'is_deleted': True})
    db.commit()

    return {'detail': 'El puesto se eliminó correctamente.'}
