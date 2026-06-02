from django.shortcuts import redirect, render
from . import models

# Create your views here.
def index(request):
    context = {
        'users' : models.User.objects.all()
    }
    return render(request,'index.html',context)

def create(request):
    user = models.User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email = request.POST['email'],age = request.POST['age'])
    user.save()
    return redirect('/')