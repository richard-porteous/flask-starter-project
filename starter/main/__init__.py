from flask import Blueprint

bp = Blueprint('main', __name__)

from starter.main import routes
