import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'change-me')
    DEBUG = os.environ.get('FLASK_DEBUG', '0') == '1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///database.db')
    CACHE_TYPE = os.environ.get('CACHE_TYPE', 'simple')
