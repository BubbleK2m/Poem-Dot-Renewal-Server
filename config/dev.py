from config import Config


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://localhost:5432/poem?' \
                              'user=postgres&password=ehdgus0608'

