from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User


class RegisterSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True, min_length=8)
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["phone", "first_name", "last_name", "password", "confirm_password"]

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        phone = attrs.get("phone")

        validate_password(password)

        if password != confirm_password:
            raise serializers.ValidationError("Пароли не совпадают!")
        
        if User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError("Такой номер уже существует!")

        return attrs

    def save(self, **kwargs):
        phone = self.validated_data["phone"]
        first_name = self.validated_data["first_name"]
        last_name = self.validated_data["last_name"]
        password = self.validated_data["password"]

        user = User(
            phone=phone,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()
        return user


class VerifyPhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(
        required=True,
    )
    code = serializers.IntegerField(
        required=True
    )

    class Meta:
        fields = ["phone", "code"]


class SendCodeSerializer(serializers.Serializer):
    phone = serializers.CharField()

    class Meta:
        fields = ["phone"]


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(
        write_only=True,
        required=True,
    )
    password = serializers.CharField(
        write_only=True,
        # min_length=8,
        required=True,
        # error_messages={"min_length": "Не менее 8 символов."},
    )
    token = serializers.CharField(read_only=True)



class UserInfoSerializer(serializers.ModelSerializer):
    qrimg = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "phone", "first_name", "last_name", "bonus_id", "bonus", "qrimg",
            "birthday", "gender", "language", "married", "status",
            "city", "children", "animal", "car", "email", "notification", "auto_brightness",
        ]

    def get_qrimg(self, obj):
        if obj.qrimg:
            return f"https://bekbekei.store{obj.qrimg.url}"


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        required=True, 
        min_length=8, 
        error_messages={"min_length": "Не менее 8 символов.", "required": "Это поле обязательно."}
    )
    confirm_password = serializers.CharField(
        required=True,
        min_length=8, 
        error_messages={"min_length": "Не менее 8 символов.", "required": "Это поле обязательно."}
    )

class ResetPasswordSerializer(serializers.Serializer):
    phone = serializers.CharField(
        required=True, 
        error_messages={"required": "Это поле обязательно."}
    )

    class Meta:
        fields = ["phone"]


class ResetPasswordVerifySerializer(serializers.Serializer):
    phone = serializers.CharField()
    code = serializers.IntegerField(
        required=True, 
        error_messages={"required": "Это поле обязательно."}
    )

    class Meta:
        fields = ["phone", "code"]


class UpdateUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["last_name", "first_name", "birthday", "gender", "language", "status", "city", "animal", "car", "married"]


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["notification", "auto_brightness", "email"]


class DeleteAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

        