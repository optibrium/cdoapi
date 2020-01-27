from com.optibrium.cdoapi.model import database
from sqlalchemy import Column, Integer, String


class Owner(database.Model):

    __tablename__ = 'owners'

    id = Column('id', Integer, primary_key=True)

    name = Column('name', String, unique=True)

    position_x = Column('position_x', Integer)

    position_y = Column('position_y', Integer)

