import pytest

from apps.api.services import generate_request

# from .fixtures import create_token


def test_api_dollar_up():
    """ Verifico si el API esta devolviendo data. """

    url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
    res = generate_request(url)

    assert len(res) == 9

# @pytest.mark.django_db
# def test_generate_token_ok():
#     """ Verifico que se estè generando el token. """
#
#     token_res = create_token('walter', '123')
#
#     print(token_res.data)
#
#     assert token_res == 'Token creado.'