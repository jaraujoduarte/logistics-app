import os
from flask_testing import TestCase
from logistics import create_app, db


class BaseTestCase(TestCase):
    def create_app(self):
        app_settings = os.getenv('APP_SETTINGS', None)
        if not app_settings:
            app_settings = 'logistics.config.DevelopmentConfig'

        app = create_app(app_settings=app_settings)
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
