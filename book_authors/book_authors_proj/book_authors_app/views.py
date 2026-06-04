from django.shortcuts import redirect, render

from book_authors_app import models

# Create your views here.
def books(request):
    context = {
        'books' : models.Book.objects.all().order_by('-created_at')
    }
    return render(request,'index.html',context)

def bookCreate(request):
    book = models.Book.objects.create(
        title=request.POST['title'],
        desc=request.POST['desc']
    )
    return redirect('/')


def bookShow(request,id):
    book = models.Book.objects.get(id=id)
    context = {
        'book' : book,
        'authors' : models.Author.objects.exclude(books=book)
    }
    return render(request,'book-show.html',context)

def deleteBook(request,id):
    book = models.Book.objects.get(id=id)
    book.delete()
    return redirect('/')

def addAuthors(request, id):
    book = models.Book.objects.get(id=id)
    author_id = request.POST.get('author')
    author = models.Author.objects.get(id=author_id)
    book.authors.add(author)
    return redirect('book-show', id=id)

def authors(request):
    context = {
        'authors' : models.Author.objects.all().order_by('-created_at')
    }
    return render(request,'authors.html',context)


def authorCreate(request):
    author = models.Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['notes']
    )
    return redirect('/authors')


def authorShow(request,id):
    author = models.Author.objects.get(id=id)
    context = {
        'author' : author,
        'books' : models.Book.objects.exclude(authors=author)
    }
    return render(request,'author-show.html',context)

def deleteAuthor(request,id):
    author = models.Author.objects.get(id=id)
    author.delete()
    return redirect('/authors')

def addBooks(request, id):
    author = models.Author.objects.get(id=id)
    book_id = request.POST.get('book')
    book = models.Book.objects.get(id=book_id)
    author.books.add(book)
    return redirect('author-show', id=id)