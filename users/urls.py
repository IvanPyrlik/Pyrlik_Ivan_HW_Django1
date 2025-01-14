from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ResetPasswordView, ConfirmRegisterView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm/', ConfirmRegisterView.as_view(), name='confirm'),
    path('reset/', ResetPasswordView.as_view(), name='reset'),
]
