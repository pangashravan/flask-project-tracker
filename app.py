import os
from flask import Flask
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
cache = Cache()


def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object('config.Config')

    db.init_app(app)
    cache.init_app(app)

    @app.route('/')
    @cache.cached(timeout=30)
    def home():
        return 'Project Tracker Running'

    return app


if __name__ == '__main__':
    app = create_app()
    debug = app.config.get('DEBUG', False)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=debug)
