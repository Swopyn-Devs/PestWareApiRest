from passlib.context import CryptContext
from passlib.hash import des_crypt


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hash:
    @staticmethod
    def bcrypt(password: str):
        return pwd_context.hash(password)

    @staticmethod
    def dcrypt(password: str):
        return des_crypt(password)

    @staticmethod
    def verify(plain_password: str, hashed_password: str):
        pwd_context
        return pwd_context.verify(plain_password, hashed_password)
