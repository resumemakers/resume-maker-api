from behave import when, then
from requests import post
from json import loads


@when('enviar o json')
def request_api_with_json(context):
    context.api_request = post(
        context.base_url + '/validate-json',
        json=loads(context.text)
    )


@then('a API deve retornar {status_code:d}')
def check_api_response(context, status_code):
    assert context.api_request.status_code == status_code
