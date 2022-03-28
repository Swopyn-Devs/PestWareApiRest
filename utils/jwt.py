from datetime import datetime, timedelta

from decouple import config
from fastapi import HTTPException, status
from jwt import encode, decode, exceptions


def expire_date(days: int):
    date = datetime.now()
    return date + timedelta(days)


def create_token(data: dict):
    token = encode(payload={**data, 'exp': expire_date(2)}, key=config('SECRET_KEY'), algorithm=config('ALGORITHM'))
    return token


def validate_token(token: str):
    try:
        decode(token, key=config('SECRET_KEY'), algorithms=[config('ALGORITHM')])
    except exceptions.DecodeError:
        raise HTTPException(detail='Token invalido.', status_code=status.HTTP_401_UNAUTHORIZED)
    except exceptions.ExpiredSignatureError:
        raise HTTPException(detail='Token expirado.', status_code=status.HTTP_401_UNAUTHORIZED)
