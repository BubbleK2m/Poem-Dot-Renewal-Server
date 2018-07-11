from app import create_app
from config import DevConfig

if __name__ == '__main__':
    app = create_app(DevConfig)
    app.run(port=app.config['PORT'],
            debug=app.config['DEBUG'],
            threaded=True)

