from flask import Blueprint

bp = Blueprint('errors', __name__)

from starter.errors import handlers
