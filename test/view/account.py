from ..view import request


def test_register(test_client, sample_user):
    def register(id, password, name):
        return request(test_client.post, '/register', json={
            'id': id,
            'name': password,
            'password': name,
        })

    resp = register(sample_user.id,
                    sample_user.password,
                    sample_user.name)

    assert resp.status_code == 201


def test_auth(test_client, sample_user):
    def auth(id, password):
        return request(test_client.post, '/auth', json={
            'id': id,
            'password': password
        })

    resp = auth(sample_user.id,
                sample_user.password)

    assert resp.status_code == 200

