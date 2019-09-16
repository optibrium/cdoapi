from com.optibrium.cdoapi.model import database
from com.optibrium.cdoapi.model import Security
from com.optibrium.cdoapi.model import User
from com.optibrium.cdoapi.model.exceptions import Forbidden, NoResultFound
from flask import Blueprint, jsonify, make_response, request

authentication = Blueprint('authentication', __name__)


@authentication.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    username = data.get('username')
    password = data.get('password')

    try:
        user = database.session \
                       .query(User) \
                       .filter(User.username == username) \
                       .one()
    except NoResultFound:
        raise Forbidden('Incorrect Username or Password')

    Security.validate_password(user, password)

    if not user.token:
        user.token = Security.generate_token()
        database.session.add(user)

    response = make_response(jsonify({'x-api-key': user.token}))
    response.set_cookie('token', user.token)
    return response


@authentication.route('/logout', methods=['GET', 'POST'])
def logout():
    cookie = request.cookies.get('token')
    api_key = request.headers.get('x-api-key')

    if cookie is not None:
        token = cookie
    elif api_key is not None:
        token = api_key
    else:
        return jsonify({'error': 'No User logged out'}), 403

    user = database.session \
                   .query(User) \
                   .filter(User.token == token) \
                   .one()
    user.token = None
    database.session.add(user)
    return '', 403
