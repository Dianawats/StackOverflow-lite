import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Parent configuration class.
    The Config class contains the general settings that
     we want all environments to have by default.
    Other environment classes inherit from it
    and can be used to set settings that are only unique to them.
     Additionally, the dictionary app_config is used to export the 
     4 environments we've specified. It's convenient to have it 
     so that we can import the config under its name tag in future.
    """

    DEBUG = False


class DevelopmentConfig(Config):
    """Configurations for Development.
    """

    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a 
       separate test database
    """

    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    """Configurations for Production.
    """

    DEBUG = False
