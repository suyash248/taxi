import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/taxi"
    RIDE_COMPLETION_DURATION_IN_SEC = 300
    DRIVER_THRESHOLD = 5
    REDIS = {
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
        "PASSWORD": None
    }

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True