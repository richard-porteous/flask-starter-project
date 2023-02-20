from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

bootstrap = Bootstrap(app)

from starter.main import bp as main_bp
app.register_blueprint(main_bp)

from starter.errors import bp as errors_bp
app.register_blueprint(errors_bp)

from starter import models

@app.shell_context_processor
def make_shell_context():
    return { 'db': db, 'User': models.User }

