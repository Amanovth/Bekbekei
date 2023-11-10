from rest_framework import generics, status, permissions
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .services import send_sms
from .models import User
from .serializers import (
    RegisterSerializers, 
    QrCodeSerializers, 
    VerifyPhoneSerializer, 
    SendCodeSerializer, 
    LoginSerializer
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            phone = serializer.data['phone']
            sms = send_sms(phone)
            if sms:
                return Response({'message': _('User registered successfully.')}, status=status.HTTP_201_CREATED)
            return Response({'message': _('Something went wrong!')}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors)


class VerifyPhoneView(generics.GenericAPIView):
    serializer_class = VerifyPhoneSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            code = serializer.data["code"]
            phone = serializer.data["phone"]

            try:
                user = User.objects.get(phone=phone)

                if user.activated:
                    return Response({"message": _("Аккаунт уже подтвержден")})
                
                if user.code == code:
                    user.activated = True
                    user.save()

                    token, created = Token.objects.get_or_create(user=user)

                    return Response(
                        {
                            "response": True,
                            "message": _("Верификация прошла успешно!"),
                            "token": token.key,
                        }
                    )
                return Response(
                    {"response": False, "message": _("Введен неверный код")}
                )
            except ObjectDoesNotExist:
                return Response(
                    {
                        "response": False,
                        "message": _("Пользователь с таким телефоном не существует"),
                    }
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class SendCodeView(generics.GenericAPIView):
    serializer_class = SendCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            phone = serializer.data["phone"]

            try:
                user = User.objects.get(phone=phone)
            except ObjectDoesNotExist:
                return Response(
                    {
                        "reponse": False,
                        "message": _("Пользователь с таким телефоном не существует"),
                    },
                )
            if not user.activated:
                user.save()

                sms = send_sms(phone)
                
                return Response(
                    {"response": True, "message": _("Код отправлен")}
                )
                
            return Response(
                {"response": False, "message": _("Аккаунт уже подтвержден")}
            )
        return Response(
            {"response": False, "detail": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            phone = request.data.get("phone")
            password = request.data.get("password")

            try:
                get_user = User.objects.get(phone=phone)
            except ObjectDoesNotExist:
                return Response(
                    {
                        "response": False,
                        "message": "Пользователь с указанными учетными данными не существует",
                    }
                )

            user = authenticate(request, phone=phone, password=password)

            if not user:
                return Response(
                    {
                        "response": False,
                        "message": "Невозможно войти в систему с указанными учетными данными",
                    }
                )

            if user.activated:
                token, created = Token.objects.get_or_create(user=user)
                return Response(
                    {
                        "response": True,
                        "isactivated": True,
                        "token": token.key,
                    }
                )
            return Response(
                {
                    "response": False,
                    "message": _("Потвердите адрес электронной почты"),
                    "isactivated": False,
                }
            )
        
        return Response(serializer.errors)

class QrCodeView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = QrCodeSerializers
