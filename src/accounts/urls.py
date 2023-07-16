from django.urls import path

from accounts.views import UserLogin, UserLogout, UserRegistration

app_name = "accounts"

urlpatterns = [
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", UserLogout.as_view(), name="logout"),
    path("registration/", UserRegistration.as_view(), name="registration"),
]
