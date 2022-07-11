from fastapi import HTTPException, status
from fastapi.responses import StreamingResponse
from fastapi_pagination import paginate, Params
from utils.messages import *

from models.job_center import JobCenter
from models.employee import Employee
from models.origin_source import OriginSource
from models.customer import Customer
from models.service_type import ServiceType
from models.price_list import PriceList
from models.price_list_plague import PriceListPlague
from models.plague import Plague
from models.plague_category import PlagueCategory
from models.indication import Indication
from models.company import Company
from models.catalog import Country
from models.job_title import JobTitle
from models.user import User
from models.business_activity import BusinessActivity
from models.extra import Extra
from models.status import Status
from models.discount import Discount
from models.quote import Quote
from models.quote_plague import QuotePlague
from models.quote_concept import QuoteConcept
from models.quote_extra import QuoteExtra
from models.rejection_reason import RejectionReason
from models.cancellation_reason import CancellationReason

from repository import customer

import pandas as pd
import base64
import uuid
import io


def get_all_data(db, model, authorize, paginate_param, filter_job_center=False, filters=False):
    if filter_job_center:
        employee = get_employee_id_by_token(db, authorize)
        data = db.query(model).filter(model.job_center_id == employee.job_center_id).filter(model.is_deleted == False).all()
    else:
        query = db.query(model).filter(model.is_deleted == False)
        query = add_filters(model, query, filters)
        data = query.all()

    # set data model to foreign field
    aux = 0
    data_main = data
    for record in data_main:
        data2 = object_as_dict(record)
        for field in data2:
            model2 = get_model(field)
            if model2 != False:
                data_model = get_data(db, model2[0], data2[field], model2[1], False, False, False)
                if field == 'customer_id':
                        data_model = customer.response_customer(db, data_model)
                data_main[aux] = update_field(data_main[aux], field, data_model)
        aux += 1
    data = data_main

    if paginate_param == True:
        return paginate(data)
    elif paginate_param == 'all':
        return data

    data_size = len(data)
    if data_size <= 0:
        data_size = 1
    return paginate(data, Params(size=data_size))


def insert_data(db, request_data):
    try:
        db.add(request_data)
        db.commit()
        db.refresh(request_data)
        return request_data.id
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=db_error())


def update_data(db, model, model_id, model_name, request_data, filters=False):
    data = get_data(db, model, model_id, model_name, True, filters, True, False)
    try:
        data.update(request_data)
        db.commit()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=db_error())

    return get_data(db, model, model_id, model_name, False, filters, True, True)


def update_delete(db, model, model_id, model_name, filters=False):
    data = get_data(db, model, model_id, model_name, True, filters, True, False)
    try:
        data.update({'is_deleted': True})
        db.commit()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=db_error())

    return {'detail': delete_message(model_name)}


def get_data(db, model, model_id=False, model_name=False, to_update=False, filters=False, is_deleted=True, foreign=True):
    if model_id is None or model_id == 'None':
        return None

    query = db.query(model)

    if model_id:
        query = query.filter(model.id == model_id)

    if is_deleted:
        query = query.filter(model.is_deleted == False)

    query = add_filters(model, query, filters)

    if to_update:
        data = query
        if not data.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=detail_message(model_name, model_id))
        return data
    else:
        data = query.first()
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=detail_message(model_name, model_id))

    data = query.all()

    # set data model to foreign field
    if foreign:
        for record in data:
            data2 = object_as_dict(record)
            for field in data2:
                model2 = get_model(field)
                if model2 != False:
                    data_model = get_data(db, model2[0], data2[field], model2[1], False, False, False)
                    if field == 'customer_id':
                        data_model = customer.response_customer(db, data_model)
                    data2[field] = data_model
        return data2
    return data


def get_employee_id_by_token(db, authorize):
    user = db.query(User).filter(
        User.id == authorize.get_jwt_subject()).filter(User.is_deleted == False)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No se encontró el perfil.')

    employee = db.query(Employee).filter(Employee.id == user.first(
    ).employee_id).filter(Employee.is_deleted == False).first()
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No se encontró el perfil.')

    return employee


def add_filters(model, query, filters):
    if filters:
        for attr, value in filters.items():
            query = query.filter(getattr(model, attr) == value)
    return query


def map_s3_url(url, field_name):
    return f"{url}/{field_name}"


def validate_pdf(file):
    allowed_types = ['application/pdf']
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='El archivo debe ser de tipo PDF: (.pdf).')


def encode_base64(data):
    return base64.b64encode(bytes(data, 'utf-8'))


def create_csv(data):
    dict_data = object_as_dict(data)
    if type(data) is list:
        df = pd.DataFrame(data=dict_data)
    else:
        df = pd.DataFrame(data=dict_data, index=[1])

    stream = io.StringIO()
    df.to_csv(stream, index=False)
    response = StreamingResponse(
        iter([stream.getvalue()]), media_type='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=export.csv'
    return response


def object_as_dict(obj):
    d = {}
    if type(obj) is list:
        for obj2 in obj:
            for column in obj2.__table__.columns:
                if column.name in d:
                    d[column.name].append(str(getattr(obj2, column.name)))
                else:
                    d[column.name] = [str(getattr(obj2, column.name))]
    else:
        for column in obj.__table__.columns:
            d[column.name] = str(getattr(obj, column.name))

    return d


def get_status_id():
    return uuid.UUID('8ba451f8-b352-4ff6-b573-532b36c7172b')


def get_model(field_name_id):
    if field_name_id == 'job_center_id':
        return [JobCenter, 'centro de trabajo']
    elif field_name_id == 'employee_id':
        return [Employee, 'empleado']
    elif field_name_id == 'origin_source_id':
        return [OriginSource, 'fuente de origen']
    elif field_name_id == 'customer_id':
        return [Customer, 'cliente']
    elif field_name_id == 'service_type_id':
        return [ServiceType, 'tipo de servicio']
    elif field_name_id == 'price_list_id':
        return [PriceList, 'lista de precio']
    elif field_name_id == 'price_list_plague_id':
        return [PriceListPlague, 'plaga de lista de precio']
    elif field_name_id == 'plague_id':
        return [Plague, 'plaga']
    elif field_name_id == 'plague_category_id':
        return [PlagueCategory, 'categoría de plaga']
    elif field_name_id == 'indication_id':
        return [Indication, 'indicación']
    elif field_name_id == 'company_id':
        return [Company, 'empresa']
    elif field_name_id == 'country_id':
        return [Country, 'país']
    elif field_name_id == 'job_title_id':
        return [JobTitle, 'puesto']
    elif field_name_id == 'business_activity_id':
        return [BusinessActivity, 'giro de la empresa']
    elif field_name_id == 'quote_id':
        return [Quote, 'cotización']
    elif field_name_id == 'quote_plague_id':
        return [QuotePlague, 'plaga de la cotización']
    elif field_name_id == 'quote_concept_id':
        return [QuoteConcept, 'concepto de la cotización']
    elif field_name_id == 'quote_extra_id':
        return [QuoteExtra, 'extra de la cotización']
    elif field_name_id == 'status_id':
        return [Status, 'estatus']
    elif field_name_id == 'discount_id':
        return [Discount, 'descuento']
    elif field_name_id == 'extra_id':
        return [Extra, 'extra']
    elif field_name_id == 'rejection_reason_id':
        return [RejectionReason, 'motivo de rechazo']
    elif field_name_id == 'cancellation_reason_id':
        return [CancellationReason, 'motivo de cancelación']

    return False


def update_field(data, field_name_id, data_model):
    if field_name_id == 'job_center_id':
        data.job_center_id = data_model
    elif field_name_id == 'country_id':
        data.country_id = data_model
    elif field_name_id == 'service_type_id':
        data.service_type_id = data_model
    elif field_name_id == 'customer_id':
        data.customer_id = data_model
    elif field_name_id == 'employee_id':
        data.employee_id = data_model
    elif field_name_id == 'origin_source_id':
        data.origin_source_id = data_model
    elif field_name_id == 'country_id':
        data.country_id = data_model
    elif field_name_id == 'job_title_id':
        data.job_title_id = data_model
    elif field_name_id == 'company_id':
        data.company_id = data_model
    elif field_name_id == 'plague_category_id':
        data.plague_category_id = data_model
    elif field_name_id == 'indication_id':
        data.indication_id = data_model
    elif field_name_id == 'business_activity_id':
        data.business_activity_id = data_model
    elif field_name_id == 'quote_id':
        data.quote_id = data_model
    elif field_name_id == 'quote_plague_id':
        data.quote_plague_id = data_model
    elif field_name_id == 'quote_concept_id':
        data.quote_concept_id = data_model
    elif field_name_id == 'quote_extra_id':
        data.quote_extra_id = data_model
    elif field_name_id == 'status_id':
        data.status_id = data_model
    elif field_name_id == 'price_list_id':
        data.price_list_id = data_model
    elif field_name_id == 'price_list_plague_id':
        data.price_list_plague_id = data_model
    elif field_name_id == 'discount_id':
        data.discount_id = data_model
    elif field_name_id == 'plague_id':
        data.plague_id = data_model
    elif field_name_id == 'plague_category_id':
        data.plague_category_id = data_model
    elif field_name_id == 'rejection_reason_id':
        data.rejection_reason_id = data_model
    elif field_name_id == 'cancellation_reason_id':
        data.cancellation_reason_id = data_model

    return data
