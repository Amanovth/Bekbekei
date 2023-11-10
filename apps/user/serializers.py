from rest_framework import serializers
from .models import User


class RegisterSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['phone', 'password', 'confirm_password']

    def save(self, **kwargs):
        phone = self.validated_data['phone']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError('Пароли не совпадают!')
        else:
            user = User(
                phone=phone,
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


class QrCodeSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['bonus', 'qrimg']