from config import DevConfig, TestConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()


def create_app(config):
    app_ = Flask(__name__)
    app_.config.from_object(config)

    db.init_app(app_)
    jwt.init_app(app_)

    with app_.app_context():
        from app import model

        if config is TestConfig:
            db.drop_all()

        db.create_all()

    from .view import Router
    Router().init_app(app_)

    return app_
