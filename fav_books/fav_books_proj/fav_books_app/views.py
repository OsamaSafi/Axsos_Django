from django.contrib import messages
from django.shortcuts import redirect, render
from . import models
import bcrypt

# Create your views here.

def index(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password_confirmation']:
            pass_hash = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode()
            user = models.User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                password = pass_hash,
            )
            messages.success(request,'user register successfully',extra_tags='alert-danger')
            return redirect('/')
        else:
            messages.error(request,'password not match',extra_tags='alert-danger')
            return redirect('/')


def login(request):
    if request.method == 'POST':
        user = models.User.objects.filter(email=request.POST['email']).first()
        if user and bcrypt.checkpw(request.POST['password'].encode(),user.password.encode()):
            request.session['user_id'] = user.id
            request.session['user_name'] = user.first_name
            messages.success(request,f'welcome {user.first_name}',extra_tags='alert-success')
            return redirect('/books')
        else:
            messages.error(request,'please enter correct psw and try again',extra_tags='alert-danger')
            return redirect('/')
        

def logout(request):
        user_name = request.session.get('user_name').capitalize()
        request.session.flush()
        messages.error(request,f'Goodbye {user_name}',extra_tags='alert-danger')
        return redirect('/')


def books(request):
    user_id = request.session.get('user_id')
    user = models.User.objects.filter(id=user_id).first()
    return render(request,'books.html',{
        'books':models.Book.objects.all(),
        'user':user
    })


def create_book(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        user = models.User.objects.filter(id=user_id).first()
        if user_id:
            book = models.Book.objects.create(
                title = request.POST['title'],
                desc = request.POST['desc'],
                upbloaded_by = user
            )
            book.users_who_likes.add(user)
            messages.success(request,'book created successfully',extra_tags='alert-success')
            return redirect('/books')
        else:
            messages.error(request,'You should login before!',extra_tags='alert-danger')
            return redirect('/')
        return redirect('/')
    else:
        messages.error(request,'something error try again',extra_tags='alert-danger')
        return redirect('/')


def book_show(request,id):
    book = models.Book.objects.filter(id=id).first()
    return render(request,'show-book.html',{
        'book': book,
        'user' : models.User.objects.filter(id=request.session.get('user_id')).first()
    })


def book_edit(request,id):
    if request.method == 'POST':
        book = models.Book.objects.filter(id=id).first()
        user_id = request.session.get('user_id')
        if book.upbloaded_by.id == user_id:
            book.title = request.POST['title']
            book.desc = request.POST['desc']
            book.save()
            messages.success(request,'book updated successfully',extra_tags='alert-success')
            return redirect(f'/books/{book.id}')
        
    else:
        messages.error(request,'something error try again',extra_tags='alert-danger')
        return redirect('/')
    

def book_delete(request,id):
    if request.method == 'POST':
        book = models.Book.objects.filter(id=id).first()
        user_id = request.session.get('user_id')
        if book.upbloaded_by.id == user_id:
            book.delete()
            messages.success(request,'book deleted successfully',extra_tags='alert-success')
            return redirect('/books')
    else:
        messages.error(request,'something error try again',extra_tags='alert-danger')
        return redirect('/')


def book_favorit(request,id):
    if request.method == 'POST':
        book = models.Book.objects.filter(id=id).first()
        user_id = request.session.get('user_id')
        user = models.User.objects.filter(id=user_id).first()
        book.users_who_likes.add(user)
        messages.success(request,'add to favorit successfully',extra_tags='alert-success')
        return redirect(f'/books/{book.id}')
    else:
        messages.error(request,'something error try again',extra_tags='alert-danger')
        return redirect('/')
    

def book_unfavorit(request,id):
    if request.method == 'POST':
        book = models.Book.objects.filter(id=id).first()
        user_id = request.session.get('user_id')
        user = models.User.objects.filter(id=user_id).first()
        if user.id == book.upbloaded_by.id:
            book.users_who_likes.remove(user)
            messages.success(request,'remove from favorit successfully',extra_tags='alert-danger')
            return redirect(f'/books/{book.id}')
        return redirect(f'/books/{book.id}')
    else:
        messages.error(request,'something error try again',extra_tags='alert-danger')
        return redirect('/')