from fastapi import HTTPException, status
from fastapi_pagination import paginate, Params
from utils.messages import *

from models.employee import Employee
from models.user import User


def get_all_data(db, model, authorize, paginate_param, filter_job_center=False):
    if filter_job_center:
        employee = get_employee_id_by_token(db, authorize)
        data = db.query(model).filter(model.job_center_id == employee.job_center_id).filter(model.is_deleted == False).all()
    else:
        data = db.query(model).filter(model.is_deleted == False).all()

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


def update_data(db, model, model_id, model_name, request_data):
    data = get_data(db, model, model_id, model_name, True)
    try:
        data.update(request_data)
        db.commit()
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=db_error())

    return data.first()


def update_delete(db, model, model_id, model_name):
    data = get_data(db, model, model_id, model_name, True)
    try:
        data.update({'is_deleted': True})
        db.commit()
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=db_error())

    return {'detail': delete_message(model_name)}


def get_data(db, model, model_id, model_name, to_update=False):
    if to_update:
        data = db.query(model).filter(model.id == model_id).filter(model.is_deleted == False)
        if not data.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail_message(model_name, model_id))
    else:
        data = db.query(model).filter(model.id == model_id).filter(model.is_deleted == False).first()
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
