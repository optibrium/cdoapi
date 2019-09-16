from com.optibrium.cdoapi.controller import application
from com.optibrium.cdoapi.model import database
import os

''' postgres://username:password@localhost '''
application.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('database_dsn')
database.init_app(application)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080, debug=True)
