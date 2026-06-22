from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('books',views.books),
    path('books/create',views.create_book),
    path('category/create',views.create_category),
    path('category/create-page',views.create_category_page),
    path('category/update/<int:id>',views.update_category,name='update_category'),
    path('category/delete/<int:id>',views.delete_category,name='delete_category'),
    path('books/update/<int:id>',views.update,name='update'),
    path('books/delete/<int:id>',views.delete_book,name='delete_book'),
    path('books/delete',views.delete_page),
]