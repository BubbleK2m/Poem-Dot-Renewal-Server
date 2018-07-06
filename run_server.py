if __name__ == '__main__':
    from app import create_app
    from config import DevConfig

    app = create_app(DevConfig)
    app.run(port=app.config['PORT'],
            debug=app.config['DEBUG'],
            threaded=True)
