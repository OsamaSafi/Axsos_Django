from django.db import models
import re


class UserManager(models.Manager):
    def reg_validate(self,data):
        errors={}
        first_name = data.get('first_name','')
        last_name = data.get('last_name','')
        email = data.get('email','')
        password = data.get('password','')
        password_confirmation = data.get('password_confirmation','')

        if len(first_name) < 2 :
            errors['first_name'] = 'First Name should at least 2 char'

        if len(last_name) < 2 :
            errors['last_name'] = 'Last Name should at least 2 char'
        
        if password != password_confirmation :
            errors['password'] = 'password should match confirm'
        elif len(password) < 8 :
            errors['password'] = 'password should at least 8 char'
        
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not email:
            errors['email'] = "Email field is required."
        elif not re.match(email_regex, email):
            errors['email'] = "Invalid email format."
        elif self.filter(email=email).exists():
            errors['email'] = "Email is already registered."
        
        return errors


    def login_validate(self,data):
        errors={}
        email = data.get('email','')
        password = data.get('password','')

        if len(password) < 8 :
            errors['password'] = 'password should at least 8 char'
        
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not email:
            errors['email'] = "Email field is required."
        elif not re.match(email_regex, email):
            errors['email'] = "Invalid email format."
        return errors
    


class BookManager(models.Manager):
    def book_validate(self,data):
        errors={}
        title = data.get('title','')
        desc = data.get('desc','')

        if not title :
            errors['title'] = 'Title field is required'
        
        if len(desc) < 5 :
            errors['desc'] = 'Description must at least 5 char'
        
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Book(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upbloaded_by = models.ForeignKey(User,related_name='books',on_delete=models.CASCADE)
    users_who_likes = models.ManyToManyField(User,related_name='liked_books')
    objects = BookManager()
