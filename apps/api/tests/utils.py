""" Importo para crear un cliente donde hacer las pruebas. """
import json

from rest_framework.test import APIClient

""" Defino los tipos de datos a manejar en las pruebas. """
JSON_API_CONTENT_TYPE = "application/vnd.api+json"
JSON_API_ACCEPT_HEADER = "application/vnd.api+json"


def get_authenticated_client(user=None):
    client = APIClient()
    if user is not None:
        client.force_authenticate(user=user)
    return client


def get(url, params=None, headers=None, user_logged=None):
    """ Defino esta función que va a ser llamada cuando corra los test. """
    url += "?{}".format(params) if params else ''
    client = get_authenticated_client(user_logged)
    if headers is None:
        headers = {'HTTP_ACCEPT': JSON_API_ACCEPT_HEADER}

    response = client.get(url, **headers)
    return response


def post(url, data=None, content_type=JSON_API_CONTENT_TYPE, headers=None, user_logged=None):
    url = url + '/' if not url.endswith('/') else url
    client = get_authenticated_client(user_logged)
    if headers is None:
        headers = {'HTTP_ACCEPT': JSON_API_ACCEPT_HEADER}

    response = client.post(url, data=json.dumps(data), content_type=content_type, **headers)
    return response
