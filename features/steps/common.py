from behave import given, when, then
from com.optibrium.cdoapi.controller import application
from com.optibrium.cdoapi.model import database, User, Owner, Animal


test_user_id = 1337
test_token = '2089cb241585a998618f15c2f3aaf273dfbf719be3a2293dfc704477539724f8'


@given(u'a web application')
def step_impl(context):
    context.application = application
    context.application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    context.application.app_context().push()
    database.init_app(context.application)
    database.create_all(app=context.application)
    database.session.query(User).delete()
    database.session.query(Owner).delete()
    database.session.query(Animal).delete()


@when(u'I GET /{uri}/id with the id')
def step_impl(context, uri):
    context.response = context.client.get("/%s/%d" % (uri, context.id))


@when(u'I GET {uri} with the token')
def step_impl(context, uri):
    context.client.cookie_jar.clear()
    headers = {'x-api-key': context.x_api_key}
    context.response = context.client.get(uri, headers=headers)


@when(u'I GET {uri} with the Cookie')
def step_impl(context, uri):
    context.client.set_cookie('/', 'token', context.cookie)
    context.response = context.client.get(uri)


@when(u'I GET {uri}')
def step_impl(context, uri):
    context.response = context.client.get(uri)


@when(u'I POST to the {api} with the ids')
def step_impl(context, api):
    uri = api % (context.owner_id, context.pet_id)
    context.response = context.client.post(uri)


@when(u'I POST {data} to the {uri}')
def step_impl(context, data, uri):
    context.response = context.client.post(uri, data=data)
    print(context.response.data)


@when(u'I PUT {data} to the /{api}/id with the id')
def step_impl(context, data, api):
    uri = "/%s/%d" % (api, context.id)
    context.response = context.client.put(uri, data=data)


@when(u'I PUT {data} to the {uri}')
def step_impl(context, data, uri):
    context.response = context.client.put(uri, data=data)


@when(u'I DELETE {api} with the ids')
def step_impl(context, api):
    uri = api % (context.owner_id, context.pet_id)
    context.response = context.client.delete(uri)


@when(u'I DELETE /{uri}/id with the id')
def step_impl(context, uri):
    context.response = context.client.delete("/%s/%d" % (uri, context.id))


@when(u'I DELETE {uri}')
def step_impl(context, uri):
    context.response = context.client.delete(uri)


@then(u'I receive a {code:d} status')
def step_impl(context, code):
    assert code == context.response.status_code, context.response.status_code
