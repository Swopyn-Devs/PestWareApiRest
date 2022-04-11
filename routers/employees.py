from fastapi import APIRouter, Depends, status, UploadFile, BackgroundTasks
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import get_db
from repository import employee
from schemas.employee import EmployeeRequest, EmployeeResponse

router = APIRouter(
    prefix='/employees',
    tags=['👨🏻‍💼 Empleados']
)


@router.get('', status_code=status.HTTP_200_OK, response_model=Page[EmployeeResponse])
async def index(db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return employee.get_all(db)


@router.get('/{employee_id}', status_code=status.HTTP_200_OK, response_model=EmployeeResponse)
async def show(employee_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return employee.retrieve(db, employee_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=EmployeeResponse)
async def store(background_tasks: BackgroundTasks, request: EmployeeRequest, db: Session = Depends(get_db),
                authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return employee.create(db, request, background_tasks)


@router.put('/{employee_id}', status_code=status.HTTP_202_ACCEPTED, response_model=EmployeeResponse)
async def update(employee_id: UUID4, request: EmployeeRequest, db: Session = Depends(get_db),
                 authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return employee.update(db, request, employee_id)


@router.patch('/{employee_id}/avatar', status_code=status.HTTP_202_ACCEPTED, response_model=EmployeeResponse)
async def update_avatar(employee_id: UUID4, file: UploadFile, db: Session = Depends(get_db),
                        authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return employee.update_avatar(db, file, employee_id)


@router.patch('/{employee_id}/signature', status_code=status.HTTP_202_ACCEPTED, response_model=EmployeeResponse)
async def update_signature(employee_id: UUID4, file: UploadFile, db: Session = Depends(get_db),
                           authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return employee.update_signature(db, file, employee_id)


@router.delete('/{employee_id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(employee_id: UUID4, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    authorize.jwt_required()
    return employee.delete(db, employee_id)
