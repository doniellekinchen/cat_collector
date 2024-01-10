from django.urls import path
#eventually we'll be pointing to view functionality which handles our request and response
from .import views

urlpatterns = [
    #we anticipate there to be a home function within views.py
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='index'),
]