from rest_framework import serializers
from django.core.exceptions import ValidationError

from .models import User


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password', 'username', 'first_name', 'last_name', 'phone_no']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        # Check that the two password fields match
        if data['password'] != data['confirm_password']:
            raise ValidationError("The two password fields didn't match.")
        return data

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_no=validated_data['phone_no'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user