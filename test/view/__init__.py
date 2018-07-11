from app import create_app
from app.model import User
from config import TestConfig
from flask_jwt_extended import create_access_token, create_refresh_token
from pytest import fixture


@fixture(scope='session')
def sample_app():
    app = create_app(TestConfig)

    with app.app_context():
        yield app


@fixture(scope='session')
def sample_client(sample_app):
    return sample_app.test_client()


@fixture(scope='session')
def sample_user():
    return User(id='sample',
                password='sample',
                name='sample')


@fixture(scope='session')
def sample_access_token(sample_user):
    return create_access_token(sample_user.id)


@fixture(scope='session')
def sample_refresh_token(sample_user):
    return create_refresh_token(sample_user.id)


def request(method, url, token=None, *args, **kwargs):
    return method(
        url, headers={
            'Authorization': f'JWT {token}' if token else None
        },

        *args,
        **kwargs,
    )


from .account import *
from .poem import *
