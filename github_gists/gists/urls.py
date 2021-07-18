from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_username/', views.search_username, name='search_username')
]