from django.urls import path, include
from users.views import dashboard, register, modal_login

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('register/', register, name='register'),
    path('accounts/login/', modal_login, name='modal-login'),
]
