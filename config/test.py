from config import Config


class TestConfig(Config):
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'postgres://localhost:5432/poem_test?' + \
                              'user=postgres&password=ehdgus0608'

    SAMPLE_USER = {
        'id': 'sample',
        'password': 'sample',
        'name': 'sample user',
    }
