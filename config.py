import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 't0ps3cr3t'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://est:newpassword@localhost/pitcher'

class TestingConfig(Config):
    TESTING = True
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",1)
        
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}