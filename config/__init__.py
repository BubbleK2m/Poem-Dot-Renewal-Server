from datetime import timedelta
import os


class Config:
    SERVICE_NAME = "Poem"
    DEBUG = True
    HOST = 'localhost'
    PORT = os.getenv("PORT", 5000)
    SECRET_KEY = os.getenv("SECRET_KEY", "PLEASE SET YOUR SECRET KEY")

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_HEADER_TYPE = "JWT"

    SWAGGER = {
        'title': SERVICE_NAME + ' API DOCS',
        'specs_route': 'docs',
        'uiversion': 3,

        'info': {
            'title': 'API Docs',
            'description': 'API Docs for ' + SERVICE_NAME,
            'version': '1.0.0',
        },

        'host': '{}:{}'.format(HOST, PORT),
        'basePath': '/',
    }

    SQLALCHEMY_SETTING = {
        'dial': 'postgres',
        'host': 'localhost',
        'port': 5432,
        'db': 'poem',
        'user': 'postgres',
        'password': 'ehdgus0608',
    }

    SQLALCHEMY_DATABASE_URI = '{}://{}:{}/{}?user={}&password={}'.format(
        SQLALCHEMY_SETTING['dial'],
        SQLALCHEMY_SETTING['host'],
        SQLALCHEMY_SETTING['port'],
        SQLALCHEMY_SETTING['db'],
        SQLALCHEMY_SETTING['user'],
        SQLALCHEMY_SETTING['password']
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JSON_AS_ASCII = False



