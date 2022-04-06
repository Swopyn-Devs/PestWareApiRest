from typing import TypeVar, Generic
from sqlalchemy.orm import Session
from pydantic import UUID4


T = TypeVar('T')


class BaseRepo:

    @staticmethod
    def get_all(db: Session, model: Generic[T]):
        return db.query(model).all()

    @staticmethod
    def retrieve_by_id(db: Session, model: Generic[T], uuid: UUID4):
        return db.query(model).filter(model.id == uuid).first()

    @staticmethod
    def create(db: Session, model: Generic[T]):
        db.add(model)
        db.commit()
        db.refresh(model)

    @staticmethod
    def update(db: Session, model: Generic[T]):
        db.commit()
        db.refresh(model)

    @staticmethod
    def delete(db: Session, model: Generic[T]):
        db.delete(model)
        db.commit()
