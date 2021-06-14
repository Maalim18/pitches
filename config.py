import os

class Config:

    

    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:069813@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS=False



