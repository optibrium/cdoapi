from com.optibrium.cdoapi.model import database
from com.optibrium.cdoapi.model import optional_position
from com.optibrium.cdoapi.model import valid_authentication_required
from com.optibrium.cdoapi.model import valid_name_required
from com.optibrium.cdoapi.model import Animal
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
    for owner in owners:
        owner.pets = database.session \
                             .query(Animal) \
                             .filter(Animal.owner == owner.id) \
                             .all()
    return jsonify(owners), 200


@owners.route('/owners/<int:id>', methods=['GET'])
@valid_authentication_required
def read_single(id):
    owner = database.session \
                    .query(Owner) \
                    .filter(Owner.id == id) \
                    .one()
    owner.pets = database.session \
                         .query(Animal) \
                         .filter(Animal.owner == owner.id) \
                         .all()
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
@optional_position
@valid_name_required
def create_single(name, x, y, id):
    owner = database.session \
                    .query(Owner) \
                    .filter(Owner.id == id) \
                    .one()
    owner.name = name
    owner.position_x = x
    owner.position_y = y
    database.session.add(owner)
    database.session.flush()
    return '', 201


@owners.route('/owners/<int:id>', methods=['DELETE'])
@valid_authentication_required
def delete_single(id):
    database.session \
            .query(Owner) \
            .filter(Owner.id == id) \
            .delete()
    return '', 202
