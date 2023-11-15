from django.urls import path
from .views import (
    RegisterView,
    VerifyPhoneView,
    SendCodeView,
    LoginView,
    UserInfo
)

urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("verify-phone", VerifyPhoneView.as_view(), name="verify-phone"),
    path("send-code", SendCodeView.as_view(), name="send-code"),
    path("login", LoginView.as_view(), name="login"),
    path("user-info", UserInfo.as_view(), name="user-info")
]
