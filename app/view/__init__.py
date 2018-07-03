from functools import wraps
from flask import abort, request
from flask_jwt_extended import fresh_jwt_required, get_jwt_identity
from ..model.user import User


class Router:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        from ..view import account
        app.register_blueprint(account.api.blueprint)

        from ..view import poem
        app.register_blueprint(poem.api.blueprint)


def json_required(required_keys):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for key, typ in required_keys.items():
                def request_has_valid_json_item(k):
                    return k in request.json and type(request.json[k]) is typ

                if not request_has_valid_json_item(key):
                    return abort(400)

            return fn(*args, **kwargs)
        return wrapper

    return decorator


def user_required(fn):
    @wraps
    @fresh_jwt_required
    def wrapper(*args, **kwargs):
        user = User.find_by_id(get_jwt_identity())

        if user is None:
            return abort(403)

        return fn(*args, **kwargs)

    return wrapper
