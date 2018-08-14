import os


class Config (object):
    """Parent configuration class"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(24)


class DevelopmentConfiguration(Config):
    """Configurations for development"""
    DEBUG = True


class TestingConfiguration(Config):
    """Configurations for testing"""
    TESTING = True
    DEBUG = True


class ProductionConfiguration(Config):
    """Configurations for production"""
    DEBUG = False


app_config = {
    'DEFAULT': DevelopmentConfiguration,
    'TESTING': TestingConfiguration,
    'DEVELOPMENT': DevelopmentConfiguration,
    'PRODUCTION': ProductionConfiguration
}
