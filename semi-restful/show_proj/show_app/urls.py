from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('shows',views.shows),
    path('show/create-page',views.createPage),
    path('show/create',views.create),
    path('show/<int:id>/edit-page',views.editPage,name='edit-page'),
    path('show/<int:id>',views.showPage,name='show-page'),
    path('show/<int:id>/edit',views.showEdit,name='show-edit'),
    path('show/<int:id>/delete',views.showDelete,name='show-delete'),
]