# can't use FLASK_APP and FLASK_DEBUG here

import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# reads a .env file with all the environment variables that your application needs.
# don't include .env in source control
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'development-secret-key'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Logging Email
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']

    # Log to STDOUT () Heroku etc.
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    # GUNICORN - for the logging hack
    GUNICORN = os.environ.get('GUNICORN_LOGGING')
