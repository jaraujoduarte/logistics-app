import os
from flask import Flask
from flask_migrate import Migrate, migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

db = SQLAlchemy()
migrate = Migrate()

def create_app(script_info=None, app_settings=None):
    # create app
    app = Flask(__name__)

    # set config
    if not app_settings:
        app_settings = os.getenv('APP_SETTINGS', None)
        if not app_settings:
            app_settings = 'logistics.config.DevelopmentConfig'

    app.config.from_object(app_settings)

    # set extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from logistics.routes.events_r import events_bp
    app.register_blueprint(events_bp, url_prefix='/api/events')

    # register error handlers
    from logistics.utils import ApiError, handle_general_error, handle_api_error
    app.register_error_handler(HTTPException, handle_general_error)
    app.register_error_handler(Exception, handle_general_error)
    app.register_error_handler(ApiError, handle_api_error)

    # set shell context
    app.shell_context_processor({'app': app, 'db': db})

    return app