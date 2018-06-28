from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from .view import Router

db = SQLAlchemy()
jwt = JWTManager()


def create_app(config):
    app_ = Flask(__name__)
    app_.config.from_object(config)

    db.init_app(app_)
    jwt.init_app(app_)
    Router().init_app(app_)

    with app_.app_context():
        from app import model
        db.create_all()

    return app_


app = create_app(Config)
