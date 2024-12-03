# Book/serializers.py
from rest_framework import serializers
from .models import User  # Assuming you have a custom User model
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']  

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # Or your custom method for creating users
        return user  # Return the created user instance
