from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import RegisterSerializer


def register(*, request: Request) -> Response:
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()


def login(*, request: Request) -> Response:
    return None


def logout(*, request: Request) -> Response:
    return None


def reset_password(*, request: Request) -> Response:
    return None
