from com.optibrium.cdoapi.model import database
from sqlalchemy import Column, Integer, String


class User(database.Model):

    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)

    username = Column('username', String, unique=True)

    password = Column('password', String)

    token = Column('token', String, unique=True)
