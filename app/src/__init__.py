from flask import Blueprint

src = Blueprint("src", __name__, static_folder='static', template_folder='templates')

from . import views