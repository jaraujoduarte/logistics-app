import os

class BaseConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgres://user:pass@127.0.0.1:5432/logistics')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SITE_NAME = 'Hillsong logistics app'


class DevelopmentConfig(BaseConfig):
    """Development Configuration"""

    DEVELOPMENT = True


class TestingConfig(BaseConfig):
    """Testing Configuration"""

    TESTING = True


class ProductionConfig(BaseConfig):
    """Production Configuration"""
    PRODUCTION = True
