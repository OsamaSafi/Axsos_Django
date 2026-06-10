from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('courses',views.courses,name='courses'),
    path('courses/create',views.create_course),
    path('courses/<int:id>/delete-page',views.deletePage,name='delete-page'),
    path('courses/<int:id>/delete',views.delete,name='delete'),
    path('courses/<int:id>/comment-page',views.commentPage,name='comment-page'),
    path('courses/<int:id>/comment',views.comment,name='comment'),
    path('courses/<int:id>/comment-delete',views.commentDelete,name='comment-delete'),
]