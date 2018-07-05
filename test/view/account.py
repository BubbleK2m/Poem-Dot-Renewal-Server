from flask import url_for
from ..view import request


def test_register(flask_client):
    def register(id, password, name):
        return request(flask_client.post, '/auth', json={
            'id': id,
            'name': password,
            'password': name,
        })

    resp = register('sample', 'sample', 'sample')
    assert resp.status_code == 201


def test_auth(flask_client):
    def auth(id, password):
        return request(flask_client.post, url_for('auth'), json={
            'id': id,
            'password': password
        })

    resp = auth('sample', 'sample')
    assert resp.status_code == 200

