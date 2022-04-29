from fastapi import HTTPException, status
from fastapi_pagination import paginate, Params
from utils.messages import *

from models.employee import Employee
from models.user import User


def get_all_data(db, model, authorize, paginate_param, filter_job_center=False, filters=False):
    if filter_job_center:
        employee = get_employee_id_by_token(db, authorize)
        data = db.query(model).filter(model.job_center_id == employee.job_center_id).filter(model.is_deleted == False).all()
    else:
        query = db.query(model).filter(model.is_deleted == False)
        query = add_filters(query, filters)
        data = query.all()

    if paginate_param:
        return paginate(data)

    data_size = len(data)
    if data_size <= 0:
        data_size = 1
    return paginate(data, Params(size=data_size))


def insert_data(db, request_data):
    try:
        db.add(request_data)
        db.commit()
        db.refresh(request_data)
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=db_error())


def update_data(db, model, model_id, model_name, request_data, filters=False):
    data = get_data(db, model, model_id, model_name, True, filters)
    try:
        data.update(request_data)
        db.commit()
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=db_error())

    return data.first()


def update_delete(db, model, model_id, model_name, filters=False):
    data = get_data(db, model, model_id, model_name, True, filters)
    try:
        data.update({'is_deleted': True})
        db.commit()
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=db_error())

    return {'detail': delete_message(model_name)}


def get_data(db, model, model_id=False, model_name=False, to_update=False, filters=False):
    if model_id:
        query = db.query(model).filter(model.id == model_id).filter(model.is_deleted == False)
    else:
        query = db.query(model).filter(model.is_deleted == False)

    query = add_filters(query, filters)

    if to_update:
        data = query
        if not data.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail_message(model_name, model_id))
    else:
        data = query.first()
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail_message(model_name, model_id))

    return data


def get_employee_id_by_token(db, authorize):
    user = db.query(User).filter(User.id == authorize.get_jwt_subject()).filter(User.is_deleted == False)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encontró el perfil.')

    employee = db.query(Employee).filter(Employee.id == user.first().employee_id).filter(Employee.is_deleted == False).first()
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encontró el perfil.')

    return employee


def add_filters(query, filters):
    if filters:
        query.filter_by(**filters)
    return query


def map_s3_url(url, field_name):
    return f"{url}/{field_name}"


def validate_pdf(file):
    allowed_types = ['application/pdf']
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='El archivo debe ser de tipo PDF: (.pdf).')
