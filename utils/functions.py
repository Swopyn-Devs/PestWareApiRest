from fastapi import HTTPException, status
from fastapi_pagination import paginate
from utils.messages import *


def get_all_data(db, model):
    return paginate(db.query(model).all())


def insert_data(db, request_data):
    db.add(request_data)
    db.commit()
    db.refresh(request_data)


def update_data(db, model, model_id, model_name, request_data):
    data = get_data(db, model, model_id, model_name, True)
    data.update(request_data)
    db.commit()
    return data.first()


def update_delete(db, model, model_id, model_name):
    data = get_data(db, model, model_id, model_name, True)
    data.update({'is_deleted': True})
    db.commit()
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
