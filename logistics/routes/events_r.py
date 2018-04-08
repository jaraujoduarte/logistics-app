from flask import Blueprint, request, jsonify
from jinja2 import TemplateNotFound
from logistics.utils import app_token_required, success_response_obj

events_bp = Blueprint('events', __name__)

@events_bp.route('/', methods=['GET'])
@events_bp.route('/<id>', methods=['GET'])
# @app_token_required
def get_event(id=None):
    if id:
        pass
    else:
        events = [
            {
                'name': 'Our event 1',
                'desc': 'events description'
            },
            {
                'name': 'Our event 2',
                'desc': 'events description 2'
            }
        ]
        limit = request.args.get('limit')
        if limit:
            return jsonify(success_response_obj(events))
        else:
            return jsonify(success_response_obj(events))