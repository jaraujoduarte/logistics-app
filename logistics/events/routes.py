from flask import Blueprint, request, jsonify
from jinja2 import TemplateNotFound
from logistics.utils import app_token_required, success_response_obj

events_bp = Blueprint('events', __name__, template_folder='templates')

@events_bp.route('/<id>', methods=['GET'])
@app_token_required
def get_event(id):
    return jsonify(success_response_obj('Its ok'))