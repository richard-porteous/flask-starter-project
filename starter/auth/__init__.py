from flask import Blueprint

bp = Blueprint('auth', __name__)

from starter.auth import routes
