from django.urls import path
from . import views

urlpatterns = [
    path('/messages',views.allMessages),
    path('/messages/create',views.messagesCreate),
    path('/messages/<int:id>/comments/create',views.commentsCreate,name='comment_create'),
    path('/messages/<int:id>/delete',views.messagesDelete,name='message_delete'),
]