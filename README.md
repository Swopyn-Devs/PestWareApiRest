# PestWare App Api REST

[![image](https://pwa-backend.s3.us-west-1.amazonaws.com/pestware-header-gray.png)](https://pestwareapp.com)

[Swopyn Devs | Backend](./README-zh.md)

## Introduction

Bienvenido a la API REST de PestWare App 👋.

El equipo de `Swopyn Devs 👨🏻‍💻👨🏻‍💻` pone a tu disposición un amplio catálogo de recursos de tipo REST para obtener, crear, actualizar y eliminar sobre ellos,
así como la conexión entre diferentes servicios de terceros. Mediante el protocolo HTTP y utilizando como estándar de comunicación el formato JSON se establecerá
la comunicación de tu aplicación.

## Requirements

- [Python 3.8 | 3.9 | 3.10](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Uvicorn](https://www.uvicorn.org/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [FastAPI Pagination](https://pypi.org/project/fastapi-pagination/)
- [FastAPI JWT Auth](https://indominusbyte.github.io/fastapi-jwt-auth/)
- [FastAPI Mail](https://sabuhish.github.io/fastapi-mail/)
- [FastAPI Utilities](https://fastapi-utils.davidmontague.xyz/help-fastapi-utils/)
- [Sqlalchemy ORM](https://www.sqlalchemy.org/)
- [Email Validator](https://pypi.org/project/email-validator/)
- [Python Decouple](https://pypi.org/project/python-decouple/)
- [Python Slugify](https://pypi.org/project/python-slugify/)
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS CLI](https://pypi.org/project/awscli/)
- [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/)
- [Pytest](https://docs.pytest.org/en/7.1.x/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)

## Run project in local

1. Clone repo.
2. Create `.env` file.

   ```dotenv
   DATABASE_URL=mysql://root:123456@127.0.0.1:3306/fastapi-admin
   REDIS_URL=redis://localhost:6379/0
   DB_HOST=pestware-dev.cmmcgxtuschw.us-west-1.rds.amazonaws.com
   DB_PORT=5432
   DB_USERNAME=postgres
   DB_PASSWORD=wr1t3rly-84r3r-c0n3-p1l0t463
   DB_DATABASE=pestware_dev
   
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_HOURS=8
   SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
   
   AWS_KEY=AKIA4K635LKRQ4LGCOHF
   AWS_SECRET=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
   
   AWS_S3_BUCKET_COMPANIES=pwa-companies
   AWS_S3_URL_COMPANIES=https://pwa-companies.s3.us-east-2.amazonaws.com
   
   AWS_S3_BUCKET_EMPLOYEES=pwa-employees
   AWS_S3_URL_EMPLOYEES=https://pwa-employees.s3.us-east-2.amazonaws.com
   
   MAIL_USERNAME=mexcorpdev@gmail.com
   MAIL_PASSWORD=xpdemhgonwaqumsp
   MAIL_FROM=mexcorpdev@gmail.com
   MAIL_PORT=465
   MAIL_SERVER=smtp.gmail.com
   MAIL_FROM_NAME=PestWare App
   MAIL_TLS=False
   MAIL_SSL=True
   USE_CREDENTIALS=True
   VALIDATE_CERTS=False
   TEMPLATE_FOLDER=./templates/mails
   ```
3. Activate your `python 3.10 or 3.9` environment.
4. Run in your terminal.

   ```shell
   > pip install -r requirements.txt
   
   > uvicorn main:app --reload
   ```

5. Visit <http://localhost:8000/docs>

## Deployment Workflow

You can check a `development` envirnoment [here](https://api.dev.pestwareapp.tech).

- username: `admin@swopyn.com`
- password: `1234567890`

You can check a `testing` envirnoment [here](https://api.test.pestwareapp.tech).

- username: `admin@swopyn.com`
- password: `1234567890`

You can check a `production` envirnoment [here](https://api.pestwareapp.tech).

- username: `admin@swopyn.com`
- password: `1234567890`

## Documentation
   
 Documentación con [Redoc](https://api.dev.pestwareapp.tech/redoc)
![](https://pwa-backend.s3.us-west-1.amazonaws.com/redoc.png)

 Documentación con [Swagger](https://api.dev.pestwareapp.tech/docs)
![](https://pwa-backend.s3.us-west-1.amazonaws.com/swagger.png)

## License

This project is licensed under the
[Apache-2.0](https://github.com/fastapi-admin/fastapi-admin/blob/master/LICENSE)
License.