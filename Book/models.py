from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from .manager import UserManager
from rest_framework import serializers

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_verification_token = models.CharField( max_length=200,null=True , blank = True)
    otp = models.CharField( max_length=4,null=True , blank = True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


    def name (self):
        return self.first_name + '   ' + self.last_name

    def __str__(self):
        return self.email
    