from flask import Blueprint

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return "Hello, CI/CD Flask.!"
