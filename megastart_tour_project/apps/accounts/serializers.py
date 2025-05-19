from rest_framework import serializers
from .models import User

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     password2 = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ['username', 'telegram_chat_id', 'password', 'password2']
#
#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError("Пароли не совпадают")
#
#         if User.objects.filter(number=attrs['number']).exists():
#             raise serializers.ValidationError({"number": "Пользователь с таким номером уже существует"})
#
#         return attrs
#
#     def create(self, validated_data):
#         validated_data.pop('password2')
#         user = User(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             number=validated_data['number'],
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'telegram_chat_id']

    def create(self, validated_data):
        if User.objects.filter(telegram_chat_id=validated_data['telegram_chat_id']).exists():
            raise serializers.ValidationError({'telegram_chat_id': 'Этот Telegram ID уже используется.'})
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            telegram_chat_id=validated_data['telegram_chat_id'],
        )


        return user
"""Келечекте бул файл өзгөрүш мүмкүн"""