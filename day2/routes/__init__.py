from flask import Blueprint

bp_app = Blueprint('main', __name__, url_prefix='/api')

from .general import home, about
from .users import users