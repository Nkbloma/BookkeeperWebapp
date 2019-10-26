import os
from flask_sqlalchemy import SQLAlchemy

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'youllnotGuess'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = 'False'