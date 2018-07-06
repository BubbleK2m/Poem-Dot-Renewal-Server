from flask import Blueprint, abort, request
from flask_restful import Api
from flask_jwt_extended import get_jwt_identity
from ..view import BaseResource, user_required, json_required
from ..model import Book, Heart, User
from sqlalchemy.exc import IntegrityError

api = Api(Blueprint(__name__, 'heart_api'))


class HeartService(BaseResource):
    @user_required
    @json_required({'value': bool})
    def put(self):
        query = request.args
        payload = request.json

        user = User.find_by_id(get_jwt_identity())
        book = Book.find_by_id(query['book_id'])

        if payload['value']:
            try:
                heart = Heart(book_id=book.id,
                              author_id=user.id)

                heart.save()

            except IntegrityError:
                return abort(409)

        else:
            heart = Heart.find_by_book_and_author_id(book.id, user.id)

            if heart is None:
                return abort(400)

            heart.remove()

        return 200

