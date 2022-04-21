from fastapi import HTTPException, status
from fastapi_pagination import paginate
from utils.messages import *

from models.employee import Employee
from models.user import User


def get_all_data(db, model, authorize):
    employee = get_employee_id_by_token(db, authorize)
    return paginate(db.query(model).filter(model.job_center_id == employee.job_center_id).all())


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
        data = db.query(model).filter(model.id == model_id)
        if not data.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail_message(model_name, model_id))
    else:
        data = db.query(model).filter(model.id == model_id).first()
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail_message(model_name, model_id))

    return data


def get_employee_id_by_token(db, authorize):
    current_user = authorize.get_jwt_subject()
    user = db.query(User).filter(User.email == current_user)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encontró el perfil.')

    return db.query(Employee).filter(Employee.id == user.first().employee_id).first()
