import traceback
from functools import wraps
from flask import Blueprint, jsonify, current_app, request

class SerializerMixin(object):

    @property
    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize for m in l]

class ApiError(Exception):
    status_code = 500

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        rv = {'error': {}}
        rv['error']['message'] = self.message
        rv['data'] = None
        return rv


def error_response_obj(error):
    response_object = {
        'data': None,
        'error': {
            'message': error
        }
    }
    return response_object


def handle_general_error(e):
    """Handler for every exception"""
    # we would capture this and sent it for report.
    traceback.print_exc()
    return jsonify(error_response_obj('Internal application error: ' + str(e))), 500


def handle_api_error(e):
    """Handler for API errors"""

    response = jsonify(e.to_dict())
    return response, e.status_code


def success_response_obj(data):
    if isinstance(data, SerializerMixin):
        message = data.serialize
    else:
        message = data

    response_object = {
        'data': message,
        'error': None
    }
    return response_object


def app_token_required(f):
    """Decorator for app token verification"""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_app.config['APP_TOKEN'] != request.headers.get('APP-TOKEN'):
            raise ApiError('Unauthorized app token another', 401)
        return f(*args, **kwargs)

    return decorated_function
