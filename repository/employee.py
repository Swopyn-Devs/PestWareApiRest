import uuid

from decouple import config
from fastapi import HTTPException, status, UploadFile, BackgroundTasks
from fastapi_pagination import paginate
from fastapi_mail import FastMail, MessageSchema
from pydantic import UUID4
from sqlalchemy.orm import Session

from repository.base import BaseRepo
from models.employee import Employee
from models.user import User
from schemas.employee import EmployeeRequest
from services import aws
from utils.hashing import Hash
from services import mail


def get_all(db: Session):
    employees = BaseRepo.get_all(db, Employee)
    data = []
    for employee in employees:
        data.append(map_s3_url(employee))

    return paginate(data)


def retrieve(db: Session, employee_id: UUID4):
    employee = BaseRepo.retrieve_by_id(db, Employee, employee_id)
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El empleado con el id {employee_id} no está disponible.')

    return map_s3_url(employee)


def create(db: Session, request: EmployeeRequest, background_tasks: BackgroundTasks):
    # validated user
    user = db.query(User).filter(User.email == request.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Ya existe una cuenta con este correo.')

    new_employee = Employee(
        name=request.name,
        company_id=request.company_id,
        job_center_id=request.job_center_id,
        job_title_id=request.job_title_id,
        color=request.color
    )
    BaseRepo.create(db, new_employee)

    # Create an account user.
    password_temp = str(uuid.uuid1()).split('-')[0]
    new_user = User(
        email=request.email,
        password=Hash.bcrypt(password_temp),
        employee_id=new_employee.id,
        is_verified=True,
        is_active=True
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Send welcome mail.
    conf = mail.conf
    data = {'name': request.name, 'email': request.email, 'password': password_temp}

    message = MessageSchema(
        subject="Bienvenido a PestWare App",
        recipients=[request.email],
        template_body=data,
        subtype='html'
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message, template_name='mail_welcome.html')

    return new_employee


def update(db: Session, request: EmployeeRequest, employee_id: UUID4):
    employee = db.query(Employee).filter(Employee.id == employee_id)
    if not employee.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El empleado con el id {employee_id} no está disponible.')

    employee.update(request.dict())
    db.commit()

    return employee.first()


def update_avatar(db: Session, avatar: UploadFile, employee_id: UUID4):
    employee = db.query(Employee).filter(Employee.id == employee_id)
    if not employee.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El empleado con el id {employee_id} no está disponible.')

    validate_image(avatar)

    # Upload file to AWS S3
    key = f'avatars/{employee_id}.jpeg'
    if not aws.upload_image(config('AWS_S3_BUCKET_EMPLOYEES'), key, avatar):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f'No fue posible actualizar la foto de perfil.')

    employee.update({'avatar': key})
    db.commit()

    return map_s3_url(employee.first())


def update_signature(db: Session, signature: UploadFile, employee_id: UUID4):
    employee = db.query(Employee).filter(Employee.id == employee_id)
    if not employee.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El empleado con el id {employee_id} no está disponible.')

    validate_image(signature)

    # Upload file to AWS S3
    key = f'signatures/{employee_id}.jpeg'
    if not aws.upload_image(config('AWS_S3_BUCKET_EMPLOYEES'), key, signature):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f'No fue posible actualizar la firma.')

    employee.update({'signature': key})
    db.commit()

    return map_s3_url(employee.first())


def delete(db: Session, employee_id: UUID4):
    employee = db.query(Employee).filter(Employee.id == employee_id)
    if not employee.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El empleado con el id {employee_id} no está disponible.')

    employee.update({'is_deleted': True})
    db.commit()

    return {'detail': 'El empleado se elimino correctamente.'}


def map_s3_url(employee: Employee):
    if employee.avatar is not None:
        employee.avatar = f"{config('AWS_S3_URL_EMPLOYEES')}/{employee.avatar}"
    if employee.signature is not None:
        employee.signature = f"{config('AWS_S3_URL_EMPLOYEES')}/{employee.signature}"

    return employee


def validate_image(image):
    allowed_types = ['image/jpeg', 'image/jpg']
    if image.content_type not in allowed_types:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='El avatar debe ser de tipo imagen: (.jpg o .jpeg).')
