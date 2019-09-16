from flask_sqlalchemy import SQLAlchemy

''' usage: app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db' '''
database = SQLAlchemy(session_options={'autocommit': True, 'autoflush': True})
