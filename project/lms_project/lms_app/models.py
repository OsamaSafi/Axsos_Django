from django.db import models

from users.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Book(models.Model):

    status_book = {
        ('free','free'),
        ('rental','rental'),
        ('sold','sold'),
    }
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250,null=True,blank=True)
    book_img = models.ImageField(upload_to='images',null=True,blank=True)
    author_img = models.ImageField(upload_to='images',null=True,blank=True)
    pages = models.IntegerField(null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    rental_price_day = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    rental_period = models.IntegerField(null=True,blank=True)
    total_rental = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=250,choices=status_book,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title