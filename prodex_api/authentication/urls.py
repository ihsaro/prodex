from django.urls import path
from . import api

urlpatterns = [
    path('register/v1/', api.RegisterAPI.as_view(), name='authentication_register_v1'),
    path('v1/login/', api.LoginAPI.as_view(), name='authentication_login_v1'),
    path('logout/v1/', api.LogoutAPI.as_view(), name='authentication_logout_v1'),
    path('reset-password/v1/', api.ResetPasswordAPI.as_view(), name='authentication_reset_password_v1'),
]
