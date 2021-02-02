from django.urls import path
from . import apis

urlpatterns = [
    path('register/v1/', apis.Register.as_view(), name='authentication_register_v1'),
    path('login/v1/', apis.Login.as_view(), name='authentication_login_v1'),
    path('logout/v1/', apis.Logout.as_view(), name='authentication_logout_v1'),
    path('reset-password/v1/', apis.ResetPassword.as_view(), name='authentication_reset_password_v1'),
]
