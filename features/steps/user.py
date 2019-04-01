import json
from behave import *
from nose.tools import assert_equal
from app.app import app
from app.views import USERS


@given(u'flask is setup')
def step_impl(context):
    assert context.client


@given(u'some users are in the system')
def step_impl(context):
    USERS.update({'bob01': {'name': 'Robert Sale'}})


@when(u'I retrieve the customer {user}')
def step_impl(context, user):
    context.res = context.client.get('/users/{}'.format(user))


@then(u'I should get a {status_code} as response status code')
def step_impl(context, status_code):
    assert_equal(context.res.status_code, int(status_code))


@then(u'the following user details are returned')
def step_impl(context):
    for row in context.table:
        assert_equal(row['name'], json.loads(
            context.res.data.decode('utf-8'))['name'])
