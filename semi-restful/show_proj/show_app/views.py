from django.shortcuts import redirect, render
from . import models
from django.contrib import messages

# Create your views here.
def index(request):
    return redirect('/shows')


def shows(request):
    context = {
        'shows' : models.Show.objects.all()
    }
    return render(request,'index.html',context)


def createPage(request):
    return render(request,'create.html')

def editPage(request,id):
    show = models.Show.objects.get(id=id)
    context = {
        'show' : show
    }
    return render(request,'edit.html',context)


def create(request):
    if request.method == "POST":
        errors = models.Show.objects.validate_show(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            
            return redirect('/show/create-page') 
            
        show = models.Show.objects.create_show(request.POST)
        return redirect('show-page', id=show.id)
    else:
        return redirect('/')


def showPage(request,id):
    show = models.Show.objects.get(id=id)
    context={
        'show':show
    }
    return render(request,'show-page.html',context)

def showEdit(request,id):
    if request.method == "POST":
        show = models.Show.objects.update_show(request.POST,id)
        return redirect('show-page',id=show.id)
    else:
        return redirect('/')


def showDelete(request,id):
    if request.method == "POST":
        models.Show.objects.delete_show(id)
        return redirect('/shows')
    else:
        return redirect('/shows')