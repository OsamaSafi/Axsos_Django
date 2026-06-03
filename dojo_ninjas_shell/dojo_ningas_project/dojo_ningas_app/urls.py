
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index),
    path('dojo/create',views.dojoCreate),
    path('ninja/create',views.ninjaCreate),
    path('dojo/<int:id>/delete',views.dojoDelete,name="dojo_delete"),
]