from flask import Blueprint, request, jsonify
from jinja2 import TemplateNotFound
from logistics.utils import app_token_required, success_response_obj

events_bp = Blueprint('events', __name__)

@events_bp.route('/', methods=['GET'])
@events_bp.route('/<id>', methods=['GET'])
@app_token_required
def get_event(id):
    if id:
        # get single event
        pass
    else:
        limit = request.args.get('limit')
        if limit:
            pass
        else:
            pass
    return jsonify(success_response_obj('Its ok'))