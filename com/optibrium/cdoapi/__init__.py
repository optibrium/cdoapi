''' This allows importing of the server from this module '''
from com.optibrium.cdoapi.controller.server import application as server
from com.optibrium.cdoapi.model import database
import os


def newApplication():
    ''' postgres://username:password@localhost '''
    server.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE')
    server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    server.app_context().push()
    database.init_app(server)
    return server


application = newApplication()
