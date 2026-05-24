from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    context = {
        'message':'placeholder to display a new form to create a new blog'
    }
    return render(request,'index.html',context)

def new(request):
    context = {
        'message':'placeholder to display a new form to create a new blog'
    }
    return render(request,'index.html',context)

def create(request):
    return redirect('/blogs')

def show(request,number):
    context = {
        'message':f'placeholder to display blog number: {number}'
    }
    return render(request,'index.html',context)

def edit(request,number):
    context = {
        'message':f'placeholder to edit blog {number}'
    }
    return render(request,'index.html',context)


def destroy(request,number):
    return redirect('/blogs')

