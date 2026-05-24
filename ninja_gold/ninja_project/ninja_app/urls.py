from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('process_money/<str:type>', views.process_money,name="process"),
]
