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
    SQLALCHEMY_DATABASE_URI = "postgres://nrnwcdimbpjbqg:7831089f7d0f099618f7e575ce57d4d06ace53f4d8aea421cfe3966f731e8f79@ec2-107-21-201-57.compute-1.amazonaws.com:5432/dapr35hpmrr1rq"


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True