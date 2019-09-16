from com.optibrium.cdoapi.model import database
from com.optibrium.cdoapi.model import valid_authentication_required
from com.optibrium.cdoapi.model import valid_name_required
from com.optibrium.cdoapi.model import Owner
from com.optibrium.cdoapi.view import jsonify
from flask import Blueprint

owners = Blueprint('owners', __name__)


@owners.route('/owners', methods=['GET'])
@valid_authentication_required
def read():
    owners = database.session \
                     .query(Owner) \
                     .all()
    return jsonify(owners), 200


@owners.route('/owners/<int:id>', methods=['GET'])
@valid_authentication_required
def read_single(id):
    owner = database.session \
                    .query(Owner) \
                    .filter(Owner.id == id) \
                    .one()
    return jsonify(owner), 200


@owners.route('/owners', methods=['POST'])
@valid_authentication_required
@valid_name_required
def create(name):
    owner = Owner(name=name)
    database.session.add(owner)
    database.session.flush()
    return jsonify(owner), 201


@owners.route('/owners/<int:id>', methods=['PUT'])
@valid_authentication_required
@valid_name_required
def create_single(name, id):
    owner = database.session \
                    .query(Owner) \
                    .filter(Owner.id == id) \
                    .one()
    owner.name = name
    database.session.add(owner)
    return '', 201


@owners.route('/owners/<int:id>', methods=['DELETE'])
@valid_authentication_required
def delete_single(id):
    database.session \
            .query(Owner) \
            .filter(Owner.id == id) \
            .delete()
    return '', 202
