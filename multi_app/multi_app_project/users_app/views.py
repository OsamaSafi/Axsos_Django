from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def register(request):
    return HttpResponse('placeholder for users to create a new user record')

def login(request):
    return HttpResponse('placeholder for users to log in.')

def new(request):
    return HttpResponse('placeholder for users to create a new user record')

def users(request):
    return HttpResponse('placeholder to display all the list of users later.')