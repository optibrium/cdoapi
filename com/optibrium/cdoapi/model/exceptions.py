from werkzeug.exceptions import NotFound  # noqa: F401
from werkzeug.exceptions import MethodNotAllowed  # noqa: F401
from sqlalchemy.orm.exc import NoResultFound  # noqa: F401
from sqlalchemy.exc import IntegrityError  # noqa: F401


class Invalid(Exception):
    '''This is when a user has supplied invalid input'''
    def __init__(self, message=''):
        self.message = message


class Forbidden(Exception):
    '''This is when a user is not permitted to access a resource'''
    def __init__(self, message=''):
        self.message = message
