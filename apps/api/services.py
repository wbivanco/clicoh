import requests


def generate_request(url):
    """
    Obtiene la respuesta de la url de los parametros que se recibe la función,  verifica si la misma es correcta y si es
    así devuelve la misma en un json.
    """

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()


def get_dollar_blue_value():
    """
    Obtiene el valor del dolar.
    """

    url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
    response = generate_request(url)

    if response:
        for res in response:
            if res.get('casa').get('nombre') == "Dolar Blue":
                return res.get('casa').get('venta')
    return ''
