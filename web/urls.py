from unicodedata import name
from django.urls import path

from . import views

app_name='web'

urlpatterns = [
    path('', views.index,name='index'),
    path('under-construction/',views.construction,name='construction')
]