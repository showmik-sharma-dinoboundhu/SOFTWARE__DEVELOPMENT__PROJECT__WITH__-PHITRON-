from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('add/', views.add_author, name='add_author')
]