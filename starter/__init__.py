from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
bootstrap = Bootstrap()

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bootstrap.init_app(app)

    from starter.main import bp as main_bp
    app.register_blueprint(main_bp)

    from starter.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from starter.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    # app.testing is true during unit tests
    if not app.debug and not app.testing:
        # logging setup
        pass

    return app

from starter import models

