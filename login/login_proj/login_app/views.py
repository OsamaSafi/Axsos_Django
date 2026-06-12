from django.contrib import messages
from django.shortcuts import redirect, render
from . import models
import bcrypt

# Create your views here.
def index(request):
    return redirect('/home')


def home(request):
    context={
        'users':models.User.objects.all()
    }
    return render(request,'index.html',context)


def register(request):
    if request.method == 'POST':
        if request.POST['password'] != request.POST['password_confirmation']:
            messages.error(request, "both password doesnt correct!", extra_tags='password_error')
            return redirect('/home')
        errors = models.User.objects.userValidate(request.POST)
        for k,v in errors.items():
            messages.error(request,v,extra_tags='register_error')
            return redirect('/home')
        models.User.objects.createUser(request.POST)
        return redirect('/home')
    messages.error(request, "error!", extra_tags='general_error')
    return('/home')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = models.User.objects.filter(email=email)
        errors = models.User.objects.userValidate(request.POST)
        for k,v in errors.items():
            messages.error(request,v,extra_tags='register_error')
            return redirect('/home')
        if len(user) > 0:
            if bcrypt.checkpw(password.encode(),user[0].password.encode()):
                request.session['user_id'] = user[0].id
                request.session['user_name'] = user[0].first_name + user[0].last_name
                messages.success(request, "login successfully!", extra_tags='login_success')
                return redirect(f'/login-page/{user[0].id}')
            else:
                messages.error(request, "password doesnt correct!", extra_tags='login_password_error')
                return redirect('/home')
    messages.error(request, "error!", extra_tags='general_error')
    return redirect('/home')


def user_delete(request,id):
    users = models.User.objects.filter(id=id)
    if len(users)>0:
        users[0].delete()
        messages.error(request, "delete user successfully!", extra_tags='delete_user')
        return redirect('/home')
    else:
        return redirect('/home')
    
def login_page(request,id):
    users = models.User.objects.filter(id=id)
    context={
        'user':users[0]
    }
    return render(request,'login-page.html',context)


def logout(request):
    request.session.flush()
    return redirect('/home')