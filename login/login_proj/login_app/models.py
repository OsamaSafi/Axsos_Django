from django.db import models
from django.contrib import messages
import bcrypt
from datetime import date
import re

class UserManager(models.Manager):
    def createUser(self,data):
        hash_password = bcrypt.hashpw(data.get('password','').encode(),bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name = data.get('first_name',''),
            last_name = data.get('last_name',''),
            email = data.get('email',''),
            birthday = data.get('birthday',''),
            password = hash_password,
        )
        return user
    
    def userValidate(self, data):
        errors = {}
        first_name = data.get('first_name', '').strip()
        last_name = data.get('last_name', '').strip()
        email = data.get('email', '').strip()
        password = data.get('password', '')
        birth_date = data.get('birthday', '')

        if len(first_name) < 2:
            errors['first_name'] = "First name must be greater than 2 characters."

        if len(last_name) < 2:
            errors['last_name'] = "Last name must be greater than 2 characters."

        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not email:
            errors['email'] = "Email field is required."
        elif not re.match(email_regex, email):
            errors['email'] = "Invalid email format."
        elif self.filter(email=email).exists():
            errors['email'] = "Email is already registered."

        if len(password) < 8:
            errors['password'] = "Password must be at least 8 characters long."

        if not birth_date:
            errors['birth_date'] = "Birth date field is required."
        else:
            try:
                if isinstance(birth_date, str):
                    input_date = date.fromisoformat(birth_date)
                else:
                    input_date = birth_date
                    
                today = date.today()
                
                if input_date >= today:
                    errors['birth_date'] = "Birth date must be in the past."
                else:
                    age = today.year - input_date.year - ((today.month, today.day) < (input_date.month, input_date.day))
                    if age < 13:
                        errors['birth_date'] = "You must be at least 13 years old to register."
                        
            except ValueError:
                errors['birth_date'] = "Invalid date format. Use YYYY-MM-DD."

        return errors





class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
