from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User
from .services import os_getbalance


class RegisterSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True, min_length=8)
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone = serializers.CharField(
        required=True, 
        min_length=19,
        error_messages={"min_length": "Введите правильный номер"},
    )

    class Meta:
        model = User
        fields = ["phone", "first_name", "last_name", "password", "confirm_password"]

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")

        attrs["phone"] = f"{''.join(filter(str.isdigit, attrs.get('phone')))}"

        validate_password(password)

        if password != confirm_password:
            raise serializers.ValidationError("Пароли не совпадают!")
        
        if User.objects.filter(phone=attrs.get("phone")).exists():
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

    def validate(self, attrs):
        attrs["phone"] = f"{''.join(filter(str.isdigit, attrs.get('phone')))}"
        return super().validate(attrs)


class SendCodeSerializer(serializers.Serializer):
    phone = serializers.CharField()

    class Meta:
        fields = ["phone"]

    def validate(self, attrs):
        return super().validate(attrs)


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

    def validate(self, attrs):
        attrs['phone'] = f"{''.join(filter(str.isdigit, attrs.get('phone')))}"
        return super().validate(attrs)



class UserInfoSerializer(serializers.ModelSerializer):
    qrimg = serializers.SerializerMethodField()
    bonus = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "user_roll",
            "phone", "first_name", "last_name", "bonus_id", "bonus", "qrimg",
            "birthday", "gender", "language", "married", "status",
            "city", "children", "animal", "car", "email", "notification", "auto_brightness",
        ]

    def get_qrimg(self, obj):
        if obj.qrimg:
            return f"https://bekbekei.store{obj.qrimg.url}"

    def get_bonus(self, obj):
        user_id = obj.id
        return os_getbalance(user_id)


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

    def validate(self, attrs):
        return super().validate(attrs)


class ResetPasswordVerifySerializer(serializers.Serializer):
    phone = serializers.CharField()
    code = serializers.IntegerField(
        required=True, 
        error_messages={"required": "Это поле обязательно."}
    )

    class Meta:
        fields = ["phone", "code"]

    def validate(self, attrs):
        return super().validate(attrs)


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

        