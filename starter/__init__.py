from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

import logging
from logging.handlers import SMTPHandler
from logging.handlers import RotatingFileHandler
import os
from starter.gunicorn_logging_hack import gunicorn_logging_hack

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
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'], subject='Microblog Failure',
                credentials=auth, secure=secure)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)


        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)           
        elif app.config['GUNICORN_LOGGING']:
            gunicorn_handler = gunicorn_logging_hack(app)
            gunicorn_handler.setLevel(logging.DEBUG)
            app.logger.addHandler(gunicorn_handler)
            # app.logger.setLevel(logging.DEBUG)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/starter.log', maxBytes=10240,
                                            backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        # DEBUG, INFO, WARNING, ERROR and CRITICAL in increasing order of severity
        app.logger.setLevel(logging.INFO)
        app.logger.info('Application startup')

    return app

from starter import models

