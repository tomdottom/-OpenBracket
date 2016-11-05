import os

class Config(object):
    """
    Base configuration, extended by classes below. 
    """
    VERSION = '0.1.0'
    DEBUG = True
    SSL = False
    SECURITY_TRACKABLE = True
    SECRET_KEY = 'This is not a good secret key.'

    CENSUS_CSV_DIRECTORY = '/home/chris/projects/de_scrape/de_contributions/'

    SQLALCHEMY_DATABASE_URI = 'mysql://ob_census_user:ob_census_pass@localhost/ob_census?charset=utf8&use_unicode=1';
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    SQLALCHEMY_TRACK_MODIFICATIONS = True


class LocalConfig(Config):
    """
    Config used when running locally
    """
    DEBUG = True
    #TESTING = True

class DevelopmentConfig(Config):
    """
    Config used on the development server. 
    """
    DEBUG = True
    #TESTING = False

class TestingConfig(Config):
    """
    Config used when running tests
    """
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    """
    Config used in production. 
    """
    DEBUG = False
    #TESTING = False
