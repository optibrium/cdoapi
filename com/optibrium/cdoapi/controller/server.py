from flask import Flask, jsonify
from flask_cors import CORS
from com.optibrium.cdoapi.controller.animals import animals
from com.optibrium.cdoapi.controller.authentication import authentication
from com.optibrium.cdoapi.controller.owners import owners
from com.optibrium.cdoapi.controller.ownership import ownership
from com.optibrium.cdoapi.model.exceptions import Forbidden
from com.optibrium.cdoapi.model.exceptions import IntegrityError
from com.optibrium.cdoapi.model.exceptions import Invalid
from com.optibrium.cdoapi.model.exceptions import NotFound
from com.optibrium.cdoapi.model.exceptions import NoResultFound
from com.optibrium.cdoapi.model.exceptions import MethodNotAllowed
from com.optibrium.cdoapi.model import valid_authentication_required

application = Flask(__name__)

application.register_blueprint(authentication)
application.register_blueprint(owners)
application.register_blueprint(animals)
application.register_blueprint(ownership)

CORS(application)


@application.route('/')
def healthcheck():
    return '1', 200


@application.route('/authcheck')
@valid_authentication_required
def authcheck():
    return '1', 200


@application.errorhandler(Exception)
def handle_error(error):

    import traceback
    traceback.print_exc()

    if isinstance(error, Invalid):
        return jsonify({'error': "Invalid input"}), 400

    if isinstance(error, Forbidden):
        return jsonify({'error': error.message}), 403

    if isinstance(error, NoResultFound):
        return jsonify({'error': 'not found'}), 404

    if isinstance(error, NotFound):
        return jsonify({'error': 'endpoint not found'}), 404

    if isinstance(error, MethodNotAllowed):
        return jsonify({'error': 'endpoint not found'}), 404

    if isinstance(error, IntegrityError):
        return jsonify({'error': 'Name exists'}), 409

    return jsonify({'error': 'please check log'}), 500
