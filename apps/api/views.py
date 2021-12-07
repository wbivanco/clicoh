from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


def generate_token(username, password):
    """ Genero el token y lo devuelvo. Está en un método separado para poder ser reutilzado. """

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario inválido.")

    password_valid = check_password(password, user.password)

    if not password_valid:
        return Response("Contraseña inválida.")

    token, _ = Token.objects.get_or_create(user=user)

    return token


@api_view(['POST'])
def login(request):
    """ Genero el token con el usuario y clave pasado en el request. """

    username = request.POST.get('username')
    password = request.POST.get('password')

    token = generate_token(username, password)

    return Response(token.key)
