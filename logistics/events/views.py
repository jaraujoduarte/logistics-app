from flask import Blueprint, request

events_bp = Blueprint('events', __name__, template_folder='templates')

@events_bp.before_request
def restrict_bp_to_auth():
    if not True:
        return redirect('general.login')