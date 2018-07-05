from app import create_app
from config import Config
from pytest import fixture


@fixture(scope='session')
def flask_app():
    app = create_app(Config)

    with app.app_context():
        yield app


@fixture(scope='session')
def flask_client(flask_app):
    return flask_app.test_client()


def request(method, url, *args, **kwargs):
    return method(
        url,
        *args,
        **kwargs,
    )


def test_auth(flask_client):
    def auth(id, password):
        return request(flask_client.post, '/auth', json={
            'id': id,
            'password': password
        })

    resp = auth('sample', 'sample')
    assert resp.status_code == 204


