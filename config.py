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
