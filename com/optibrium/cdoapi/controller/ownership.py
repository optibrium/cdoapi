from com.optibrium.cdoapi.model import database
from com.optibrium.cdoapi.model import valid_authentication_required
from com.optibrium.cdoapi.model import Animal
from flask import Blueprint

ownership = Blueprint('ownership', __name__)


@ownership.route('/owner/<int:owner>/pet/<int:pet>', methods=['POST'])
@valid_authentication_required
def create(owner, pet):
    animal = database.session \
                     .query(Animal) \
                     .filter(Animal.id == pet) \
                     .one()
    animal.owner = owner
    database.session.add(animal)
    database.session.flush()
    return '', 201


@ownership.route('/owner/<int:owner>/pet/<int:pet>', methods=['DELETE'])
@valid_authentication_required
def delete(owner, pet):
    animal = database.session \
                     .query(Animal) \
                     .filter(Animal.id == pet) \
                     .filter(Animal.owner == owner) \
                     .one()
    animal.owner = None
    database.session.add(animal)
    database.session.flush()
    return '', 202
