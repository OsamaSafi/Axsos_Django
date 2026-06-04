from django.urls import path
from . import views

urlpatterns = [
    path('',views.books),
    path('book/create',views.bookCreate),
    path('book/<int:id>',views.bookShow,name='book-show'),
    path('book/<int:id>/add',views.addAuthors,name='add-author'),
    path('book/<int:id>/delete',views.deleteBook,name='delete-book'),

    path('authors',views.authors),
    path('author/create',views.authorCreate),
    path('author/<int:id>',views.authorShow,name='author-show'),
    path('author/<int:id>/add',views.addBooks,name='add-book'),
    path('author/<int:id>/delete',views.deleteAuthor,name='delete-author'),
]