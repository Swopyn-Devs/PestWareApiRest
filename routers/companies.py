from typing import List

from fastapi import APIRouter, Depends, status, UploadFile
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import get_db
from repository import company
from schemas.company import CompanyRequest, CompanyResponse

router = APIRouter(
    prefix='/companies',
    tags=['🏢 Empresas']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=List[CompanyResponse])
async def index(db: Session = Depends(get_db)):
    return company.get_all(db)


@router.get('/{company_id}', status_code=status.HTTP_200_OK, response_model=CompanyResponse)
async def show(company_id: UUID4, db: Session = Depends(get_db)):
    return company.retrieve(db, company_id)


@router.put('/{company_id}', status_code=status.HTTP_202_ACCEPTED, response_model=CompanyResponse)
async def update(company_id: UUID4, request: CompanyRequest, db: Session = Depends(get_db)):
    return company.update(db, request, company_id)


@router.patch('/{company_id}/document-logo', status_code=status.HTTP_202_ACCEPTED, response_model=CompanyResponse)
async def update_document_logo(company_id: UUID4, file: UploadFile, db: Session = Depends(get_db)):
    return company.update_document_logo(db, file, company_id)


@router.patch('/{company_id}/document-stamp', status_code=status.HTTP_202_ACCEPTED, response_model=CompanyResponse)
async def update_document_stamp(company_id: UUID4, file: UploadFile, db: Session = Depends(get_db)):
    return company.update_document_stamp(db, file, company_id)


@router.patch('/{company_id}/web-logo', status_code=status.HTTP_202_ACCEPTED, response_model=CompanyResponse)
async def update_web_logo(company_id: UUID4, file: UploadFile, db: Session = Depends(get_db)):
    return company.update_web_logo(db, file, company_id)


@router.delete('/{company_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(company_id: UUID4, db: Session = Depends(get_db)):
    return company.delete(db, company_id)