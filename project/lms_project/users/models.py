from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    role_choice = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=150, choices=role_choice, default='admin')
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']