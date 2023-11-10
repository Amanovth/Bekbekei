from django.urls import path
from .views import (
    RegisterView, 
    QrCodeView, 
    VerifyPhoneView, 
    SendCodeView,
    LoginView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-phone', VerifyPhoneView.as_view(), name='verify-phone'),
    path('send-code', SendCodeView.as_view(), name='send-code'),
    path('login', LoginView.as_view(), name='login'),
    path('my-bonus/', QrCodeView.as_view(), name='Bonus')
]