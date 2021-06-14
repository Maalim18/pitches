import os

class Config:

    

    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:069813@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS=False



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
config_options={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}