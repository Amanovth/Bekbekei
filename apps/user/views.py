from rest_framework import status
from rest_framework.generics import (
    GenericAPIView,
    CreateAPIView
)
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework.views import APIView
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .services import send_sms
from .models import User
from .serializers import (
    RegisterSerializers,
    VerifyPhoneSerializer,
    SendCodeSerializer,
    LoginSerializer,
    UserInfoSerializer,
    ChangePasswordSerializer,
    ResetPasswordSerializer,
    ResetPasswordVerifySerializer,
    UpdateUserDetailSerializer
)


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            phone = serializer.data["phone"]
            user = User.objects.get(phone=phone)
            # sms = send_sms(phone, "Подтвердите номер телефона", user.code)
            # if sms:
            return Response(
                {
                    "response": True,
                    "message": _("Пользователь успешно зарегистрирован."),
                },
                status=status.HTTP_201_CREATED,
            )
            # return Response(
            #     {"response": False, "message": _("Something went wrong!")},
            #     status=status.HTTP_400_BAD_REQUEST,
            # )
        return Response(serializer.errors)


class VerifyPhoneView(GenericAPIView):
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


class SendCodeView(GenericAPIView):
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

                sms = send_sms(phone, "Ваш новый код подтверждения", user.code)

                return Response({"response": True, "message": _("Код отправлен")})

            return Response(
                {"response": False, "message": _("Аккаунт уже подтвержден")}
            )
        return Response(serializer.errors)


class LoginView(GenericAPIView):
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
                        "message": _("Пользователь с указанными учетными данными не существует"),
                    }
                )

            user = authenticate(request, phone=phone, password=password)

            if not user:
                return Response(
                    {
                        "response": False,
                        "message": _("Невозможно войти в систему с указанными учетными данными"),
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
                    "message": _("Подтвердите адрес электронной почты"),
                    "isactivated": False,
                }
            )

        return Response(serializer.errors)


class UserInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_info = UserInfoSerializer(request.user).data
        return Response(user_info)


class ChangePasswordView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        user = request.user
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            password = serializer.data["password"]
            confirm_password = serializer.data["confirm_password"]

            if password != confirm_password:
                return Response({"response": False, "message": _("Пароли не совпадают")})

            user.set_password(password)
            user.save()

            return Response({"response": False, "message": _("Пароль успешно обновлен")})
        return Response(serializer.errors)


class ResetPasswordView(GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            phone = serializer.data["phone"]
            try:
                user = User.objects.get(phone=phone)
                user.save()

                send_sms(phone, "Подтвердите номер для сброса пароля", user.code)
                return Response({"response": True, "message": _("Код подтверждения успешно отправлен")})
            except ObjectDoesNotExist:
                return Response({"response": False, "message": _("Пользователь с таким номером не существует")})
        return Response(serializer.errors)


class ResetPasswordVerifyView(GenericAPIView):
    serializer_class = ResetPasswordVerifySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            code = serializer.data["code"]
            phone = serializer.data["phone"]
            try:
                user = User.objects.get(phone=phone)

                if user.code == code:
                    token, created = Token.objects.get_or_create(user=user)

                    return Response({"response": True, "token": token.key})
                return Response({"response": False, "message": _("Введен неверный код")})
            except ObjectDoesNotExist:
                return Response({"response": False, "message": _("Пользователь с таким номером не существует")})
        return Response(serializer.errors)


class UpdateUserDetailView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateUserDetailSerializer

    def post(self, request):
        user = request.user

        serializer = self.serializer_class(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"response": True})
        return Response(serializer.errors)
