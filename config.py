import os


class Config(object):
    """
    Adds configurations to the Flask project
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
