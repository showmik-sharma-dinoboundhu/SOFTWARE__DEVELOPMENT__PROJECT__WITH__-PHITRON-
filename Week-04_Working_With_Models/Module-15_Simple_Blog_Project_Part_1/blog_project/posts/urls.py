from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_posts, name='add_posts'),
    path('edit/<int:id>', views.edit_posts, name='edit_posts'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
    
]