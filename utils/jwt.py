from datetime import datetime, timedelta

import jwt
from decouple import config
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from models.user import User

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/authentication/login')
expires = datetime.utcnow() + timedelta(hours=int(config('ACCESS_TOKEN_EXPIRE_HOURS')))


def create_access_token(user: User):
    data = {
        'user_id': str(user.id),
        'username': user.email,
        'exp': expires
    }

    return jwt.encode(payload=data, key=config('SECRET_KEY'), algorithm=config('ALGORITHM'))


def decode_access_token(token: str):
    return jwt.decode(token, key=config('SECRET_KEY'), algorithms=[config('ALGORITHM')])


def get_current_user(db: Session, token: str = Depends(oauth2_schema)):
    data = decode_access_token(token)
    return db.query(User).filter(User.id == data['user_id']).first()
