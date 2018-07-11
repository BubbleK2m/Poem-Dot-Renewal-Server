from ..view import request


def test_create_poem(sample_client, sample_access_token):
    def create_poem(title, content):
        return request(sample_client.post, '/poem', sample_access_token, json={
            'title': title,
            'content': content,
        })

    resp = create_poem('Sample Poem Title', 'Sample Poem Content')
    assert resp.status_code == 201 and resp.json['created'] == 1


def test_read_poems(sample_client, sample_access_token):
    def read_poems():
        return request(sample_client.get, '/poem', sample_access_token)

    resp = read_poems()
    assert resp.status_code == 200


def test_edit_poem(sample_client, sample_access_token):
    def edit_poem(id, title, content):
        return request(sample_client.put, '/poem', sample_access_token, json={
            'id': id,
            'title': title,
            'content': content,
        })

    resp = edit_poem(1, 'First Poem Title', 'First Poem Content')
    assert resp.status_code == 200


def test_delete_poem(sample_client, sample_access_token):
    def delete_poem(id):
        return request(sample_client.delete, '/poem', sample_access_token, json={
            'id': id,
        })

    resp = delete_poem(1)
    assert resp.status_code == 200
