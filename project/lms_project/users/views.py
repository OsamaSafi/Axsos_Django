from django.shortcuts import render, redirect
from users.form import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from users.models import User


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            messages.success(request, 'Account Created Successfully!')
            return redirect('/') 
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome Back {user.first_name}!')
                return redirect('/')
            else:
                form.add_error(None, 'email or password not correct!')
        return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')