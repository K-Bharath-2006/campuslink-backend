from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'is_student', 'is_admin']

    def validate_email(self, value):
        if not value.endswith('@sece.ac.in'):
            raise ValidationError("Email must belong to sece.ac.in domain")
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_student=True,
            is_admin=False
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if not user:
            raise serializers.ValidationError("Invalid credentials.")
        data['user'] = user
        return data
