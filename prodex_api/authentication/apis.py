from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from . import services


class Register(APIView):
    def post(self, request, format=None):
        return services.register(request=request)


class Login(APIView):
    def post(self, request, format=None):
        pass


class Logout(APIView):
    authentication_classes = [IsAuthenticated]

    def post(self, request, format=None):
        pass


class ResetPassword(APIView):
    def post(self, request, format=None):
        pass
