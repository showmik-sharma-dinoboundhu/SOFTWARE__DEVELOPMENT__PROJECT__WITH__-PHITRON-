from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_posts, name='add_posts')
]