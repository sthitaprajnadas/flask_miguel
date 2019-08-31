import os

base_dir=os.path.abspath(os.path.dirname(__file__))

class Config(object):

    #SQLALCHEMY_DATABASE_URI='sqllite:///'+os.path.join(base_dir,'blogapp.db')
    SQLALCHEMY_DATABASE_URI='sqlite:///flaskblog.db'

    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY= os.environ.get('SECRET_KEY') or 'you will never know'
