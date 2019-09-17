from behave import given, then, when
from com.optibrium.cdoapi.model import database, Animal, Owner
import json


@then(u'I receive an id')
def step_impl(context):
    assert 'id' in context.response.json, context.response.json
    assert context.response.json['id'] is not None


@when(u'I receive an id')
def step_impl(context):
    context.id = context.response.json['id']


@when(u'I receive an owner id')
def step_impl(context):
    context.owner_id = context.response.json['id']


@when(u'I receive a pet id')
def step_impl(context):
    context.pet_id = context.response.json['id']


@given(u'owners contains {json_string}')
def step_impl(context, json_string):
    for name in json.loads(json_string):
        database.session.add(Owner(name=name))


@given(u'{species}s contains {json_string}')
def step_impl(context, species, json_string):
    for name in json.loads(json_string):
        database.session.add(Animal(name=name, species=species))


@then(u'a list of names containing {json_string} is returned')
def step_impl(context, json_string):
    names = [x['name'] for x in context.response.json]
    for name in json.loads(json_string):
        assert name in names, "expected %s in %s" % (name, names)


@then(u'a owners has been created called {name}')
def step_impl(context, name):
    database.session.query(Owner).filter(Owner.name == name).one()


@then(u'a {species} has been created called {name}')
def step_impl(context, species, name):
    database.session.query(Animal).filter(Animal.name == name).one()


@then(u'the object returned has a name of {name}')
def step_impl(context, name):
    assert context.response.json['name'] == name, context.response.json
