from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
bootstrap = Bootstrap(app)

from starter.main import bp as main_bp
app.register_blueprint(main_bp)

from starter.auth import bp as auth_bp
app.register_blueprint(auth_bp)

from starter.errors import bp as errors_bp
app.register_blueprint(errors_bp)

from starter import models

