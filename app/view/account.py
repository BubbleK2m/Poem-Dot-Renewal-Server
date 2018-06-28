from flask import abort, Blueprint, request, Response
from flask_jwt_extended import *
from flask_restful import Api, Resource
from sqlalchemy.exc import IntegrityError
from ..model.user import User

api = Api(Blueprint(__name__, 'account_api'))


@api.resource('/auth')
class Auth(Resource):
    def post(self):
        data = request.json
        user = User.find_by_id(data['id'])

        if not (user and data['password'] == user.password):
            return Response(status=204)

        return {
            'access_token': create_access_token(identity=user.id),
            'refresh_token': create_refresh_token(identity=user.id),
        }


@api.resource('/register')
class Register(Resource):
    def post(self):
        data = request.json

        user = User(id=data['id'],
                    name=data['name'],
                    password=data['password'])

        try:
            user.save()

        except IntegrityError:
            return abort(409)

        return {
            'access_token': create_access_token(identity=user.id),
            'refresh_token': create_refresh_token(identity=user.id),
        }, 201


@api.resource('/refresh')
class Refresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        return {
            'access_token': create_access_token(identity=get_jwt_identity())
        }
