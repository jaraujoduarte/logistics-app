from flask import Blueprint, request, render_template
from jinja2 import TemplateNotFound

events_bp = Blueprint('events', __name__, template_folder='templates')

@events_bp.before_request
def restrict_bp_to_auth():
    if not True:
        return redirect('general.login')


@events_bp.route('/')
def home():
    try:
        return render_template('events/home.html')
    except TemplateNotFound:
        abort(404)