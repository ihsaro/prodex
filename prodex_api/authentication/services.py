from django.contrib.auth import authenticate

from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from utils.prodex_response import success_response, error_response

from .models import ProdexUser
from .serializers import RegisterSerializer


def register(*, request: Request) -> Response:
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()


def login(*, request: Request) -> Response:
    try:
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            user = ProdexUser(username=request.data['username'])
            refresh_token = RefreshToken.for_user(user)

            response = Response(success_response())

            response.set_cookie(key='refresh', value=str(refresh_token), httponly=True)
            response.set_cookie(key='access', value=str(refresh_token.access_token), httponly=True)

            return response
        else:
            return Response(error_response(errors=[{
                    'credential_error': 'Invalid credentials'
                }
            ]))
    except KeyError:
        return Response(error_response(errors=[
            {
                'key_error': 'Fields were missing'
            }
        ]))


def logout(*, request: Request) -> Response:
    return None


def reset_password(*, request: Request) -> Response:
    return None
