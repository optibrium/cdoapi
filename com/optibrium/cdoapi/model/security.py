from com.optibrium.cdoapi.model import database
from com.optibrium.cdoapi.model import User
from com.optibrium.cdoapi.model.exceptions import Forbidden, NoResultFound
import hashlib
import os


class Security:

    @staticmethod
    def validate_password(user, password):
        if not Security.hash_password(password) == user.password:
            raise Forbidden('Incorrect Username or Password')

    @staticmethod
    def generate_token():
        return hashlib.sha256(os.urandom(256)).hexdigest()

    @staticmethod
    def check_token(token):
        try:
            database.session.query(User).filter(User.token == token).one()
        except NoResultFound:
            raise Forbidden()

    @staticmethod
    def hash_password(string):
        return hashlib.sha256(string.encode()).hexdigest()
