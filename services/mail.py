from fastapi_mail import ConnectionConfig
from decouple import config


conf = ConnectionConfig(
    MAIL_USERNAME=config('MAIL_USERNAME'),
    MAIL_PASSWORD=config('MAIL_PASSWORD'),
    MAIL_FROM=config('MAIL_FROM'),
    MAIL_PORT=config('MAIL_PORT'),
    MAIL_SERVER=config('MAIL_SERVER'),
    MAIL_FROM_NAME=config('MAIL_FROM_NAME'),
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=config('MAIL_SSL'),
    USE_CREDENTIALS=config('USE_CREDENTIALS'),
    VALIDATE_CERTS=config('VALIDATE_CERTS'),
    TEMPLATE_FOLDER=config('TEMPLATE_FOLDER')
)
