from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

general_bp = Blueprint('general', __name__, template_folder='templates')

@general_bp.route('/')
def login():
    try:
        return render_template('general/login.html')
    except TemplateNotFound:
        abort(404)