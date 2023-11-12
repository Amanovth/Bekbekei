from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User


class RegisterSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["phone", "first_name", "last_name", "password", "confirm_password"]

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")

        validate_password(password)

        if password != confirm_password:
            raise serializers.ValidationError("Пароли не совпадают!")

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
    phone = serializers.CharField()
    code = serializers.IntegerField()

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


# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['phone', 'password']


# class UserDetailSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUserDetail
#         fields = ['id', 'name', 'surname', 'third_name', 'birthday',
#                   'gender', 'language',
#                   'married', 'status', 'city', 'program_lang', 'animal', 'children', 'car']


class UserInfoSerializer(serializers.ModelSerializer):
    qrimg = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "phone", "first_name", "last_name", "bonus_id", "bonus", "qrimg",
            "birthday", "gender", "language", "married", "status",
            "city", "children", "animal", "car"
        ]

    def get_qrimg(self, obj):
        if obj.qrimg:
            return f"http://89.223.126.144{obj.qrimg.url}"
