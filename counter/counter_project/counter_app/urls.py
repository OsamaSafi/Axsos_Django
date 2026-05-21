from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('destroy-session',views.destroy,name="destroy"),
    path('add-two',views.add,name="add"),
    path('increment',views.increment,name="increment"),
]