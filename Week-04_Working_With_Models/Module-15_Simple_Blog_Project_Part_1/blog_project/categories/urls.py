from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('add/', views.add_categories, name='add_categories')
]