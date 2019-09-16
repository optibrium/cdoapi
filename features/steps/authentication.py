from behave import given, when, then
from com.optibrium.cdoapi.model import database, Security, User
from common import test_token


@given(u'an unauthenticated client')
def step_impl(context):
    context.client = context.application.test_client()


@when(u'{username} and {password} correspond to a valid user')
def step_impl(context, username, password):
    database.session.add(User(
        username=username,
        password=Security.hash_password(password)))


@when(u'I have no valid users')
def step_impl(context):
    database.session.query(User).delete()


@given(u'a client with a valid authentication token')
def step_impl(context):
    context.client = context.application.test_client()
    context.client.set_cookie('/', 'token', test_token)
    user = User(username='user', password='pass', token=test_token)
    database.session.add(user)


@then(u'I receive an x-api-key')
def step_impl(context):
    assert 'x-api-key' in context.response.json
    context.x_api_key = context.response.json['x-api-key']


@then(u'a matching cookie')
def step_impl(context):
    context.cookie = list(context.client.cookie_jar)[0].value
    assert context.x_api_key == context.cookie, context.cookie


@then(u'I receive a cookie')
def step_impl(context):
    header = context.response.headers['Set-Cookie']
    assert 'token' in header, header
    context.cookie = list(context.client.cookie_jar)[0].value


@then(u'the error {error} is returned')
def step_impl(context, error):
    assert context.response.json['error'] == error, context.response.json
