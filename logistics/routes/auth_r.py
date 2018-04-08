from flask import Blueprint, request, jsonify
from jinja2 import TemplateNotFound
from logistics.utils import app_token_required, success_response_obj

auth_bp = Blueprint('auth', __name__)
