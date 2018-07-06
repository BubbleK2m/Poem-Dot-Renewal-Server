from functools import wraps
from flask import abort, Blueprint, request
from flask_restful import Api
from flask_jwt_extended import get_jwt_identity
from ..view import BaseResource, user_required, json_required
from ..model import Book, User, Poem

api = Api(Blueprint(__name__, 'book_api'))


def author_required(fn):
    @wraps(fn)
    @user_required
    @json_required({'poems': list})
    def wrapper(*args, **kwargs):
        user = User.find_by_id(get_jwt_identity())
        payload = request.json

        for pid in payload['poems']:
            poem = Poem.find_by_id(pid)

            if not (poem and not poem.book_id and poem.author_id == user.id):
                return abort(400)

        return fn(*args, **kwargs)

    return wrapper


@api.resource('/book')
class BookService(BaseResource):
    @author_required
    @json_required({'title': str, 'description': str})
    def post(self):
        payload = request.json

        book = Book(title=payload['title'],
                    description=payload['description'],
                    author_id=get_jwt_identity())

        for pid in payload['poems']:
            poem = Poem.find_by_id(pid)

            poem = Poem(title=poem.title,
                        content=poem.content,
                        author_id=poem.author_id,
                        book_id=poem.book_id)

            poem.save()

        book.save()

        return {
            'created': book.id,
        }

    @user_required
    def get(self):
        user = User.find_by_id(get_jwt_identity())
        self.unicode_json_response([b.to_dict() for b in user.books])
