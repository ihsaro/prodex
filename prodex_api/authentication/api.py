from rest_framework.views import APIView

from .services import register, login, logout, reset_password


class RegisterAPI(APIView):
    def post(self, request, format=None):
        return register(request=request)


class LoginAPI(APIView):
    def post(self, request, format=None):
        return login(request=request)


class LogoutAPI(APIView):
    def post(self, request, format=None):
        return logout(request=request)


class ResetPasswordAPI(APIView):
    def post(self, request, format=None):
        return reset_password(request=request)
