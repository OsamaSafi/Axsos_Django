from django.shortcuts import redirect, render
from lms_app.form import BookForm,CategoryForm
from . import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    return render(request,'pages/index.html',{
        'books':models.Book.objects.all(),
        'categories':models.Category.objects.all(),
        'form' : BookForm(),
        'allbooks' : models.Book.objects.filter(active=True).count(),
        'freebooks' : models.Book.objects.filter(status='free').count(),
        'soldbooks' : models.Book.objects.filter(status='sold').count(),
        'rentalbooks' : models.Book.objects.filter(status='rental').count(),
    })

@login_required
def books(request):
    search = models.Book.objects.all()
    title = ''
    if 'search_name' in request.GET:
        title = request.GET['search_name'] 
        if title:
            search = search.filter(title__icontains=title)

    return render(request,'pages/books.html',{
        'books':search,
        'categories':models.Category.objects.all()
    })


@login_required
def update_page(request):
    return render(request,'pages/update.html')


@login_required
def delete_page(request):
    return render(request,'pages/delete.html')

@login_required
def create_book(request):
    if request.method == "POST":
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
            messages.success(request, 'Book created successfully')
            return redirect('/')
        else:
            for field, errors in add_book.errors.items():
                for error in errors:
                    messages.error(request, error)
                
            return redirect('/')
            
    return redirect('/')

@login_required
def create_category_page(request):
    return render(request,'pages/create-cat.html',{
        'formcat' : CategoryForm(),
        'categories':models.Category.objects.all()
    })

@login_required
def create_category(request):
    if request.method == 'POST':
        add_category = CategoryForm(request.POST)
        if add_category.is_valid(): 
            add_category.save()
            messages.success(request, 'Category created successfully!') 
        else:
            for field, errors in add_category.errors.items():
                for error in errors:
                    messages.error(request, error)
                    
    return redirect('/category/create-page')



@login_required
def update(request,id):
    book = models.Book.objects.get(id=id)
    if request.method == "POST":
        book_save = BookForm(request.POST,request.FILES,instance=book)
        if book_save.is_valid():
            book_save.save()
            messages.success(request, 'Book Updated Successfully!') 
            return redirect(f'/books/update/{book.id}')
    else:
        book_save = BookForm(instance=book)
    return render(request,'pages/update.html',{
        'form':book_save
    })


@login_required
def delete_book(request,id):
    book = models.Book.objects.get(id=id)
    if book and request.method == "POST":
        book.delete()
        messages.success(request, 'Book Deleted Successfully!') 
        return redirect('/')
    else:
        return render(
            request,
            'pages/delete.html',
            {
                'book':book
            }
        )


@login_required
def update_category(request,id):
    cat = models.Category.objects.get(id=id)
    if request.method == "POST":
        cat_save = CategoryForm(request.POST,instance=cat)
        if cat_save.is_valid():
            cat_save.save()
            messages.success(request, 'Category Updated Successfully!') 
            return redirect('/category/create-page')
    else:
        cat_save = CategoryForm(instance=cat)
        return render(request,'pages/update-cat.html',{
            'form' : cat_save
        })
    

@login_required
def delete_category(request,id):
    cat = models.Category.objects.get(id=id)
    if request.method == 'POST':
        cat.delete()
        messages.success(request, 'Category Deleted Successfully!') 
        return redirect('/category/create-page')

