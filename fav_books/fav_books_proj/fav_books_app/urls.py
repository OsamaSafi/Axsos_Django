from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login',views.login),
    path('logout',views.logout),
    path('register',views.register),
    path('books',views.books),
    path('books/create',views.create_book),
    path('books/<int:id>',views.book_show,name='book-show'),
    path('books/<int:id>/edit',views.book_edit,name='book-edit'),
    path('books/<int:id>/destroy',views.book_delete,name='book-delete'),
    path('books/<int:id>/addfavorit',views.book_favorit,name='book-favorit'),
    path('books/<int:id>/removefavorit',views.book_unfavorit,name='book-unfavorit'),
]