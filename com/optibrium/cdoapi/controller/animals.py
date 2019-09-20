from com.optibrium.cdoapi.model import Animal
from com.optibrium.cdoapi.model import database
from com.optibrium.cdoapi.model import existent_species_required
from com.optibrium.cdoapi.model import valid_authentication_required
from com.optibrium.cdoapi.model import valid_name_required
from com.optibrium.cdoapi.view import jsonify
from flask import Blueprint

animals = Blueprint('animals', __name__)


@animals.route('/<species>s', methods=['GET'])
@valid_authentication_required
@existent_species_required
def read(species):
    animals = database.session \
                      .query(Animal) \
                      .filter(Animal.species == species) \
                      .all()
    return jsonify(animals), 200


@animals.route('/<species>s/<int:id>', methods=['GET'])
@valid_authentication_required
@existent_species_required
def read_single(species, id):
    animal = database.session \
                     .query(Animal) \
                     .filter(Animal.species == species) \
                     .filter(Animal.id == id) \
                     .one()
    return jsonify(animal), 200


@animals.route('/<species>s', methods=['POST'])
@valid_authentication_required
@valid_name_required
def create(name, species):
    animal = Animal(name=name, species=species)
    database.session.add(animal)
    database.session.flush()
    return jsonify(animal), 201


@animals.route('/<species>s/<int:id>', methods=['PUT'])
@valid_authentication_required
@valid_name_required
def create_single(name, species, id):
    animal = database.session \
                     .query(Animal) \
                     .filter(Animal.species == species) \
                     .filter(Animal.id == id) \
                     .one()
    animal.name = name
    database.session.add(animal)
    return '', 201


@animals.route('/<species>s/<int:id>', methods=['DELETE'])
@valid_authentication_required
def delete_single(species, id):
    database.session \
            .query(Animal) \
            .filter(Animal.species == species) \
            .filter(Animal.id == id) \
            .delete()
    return '', 202
