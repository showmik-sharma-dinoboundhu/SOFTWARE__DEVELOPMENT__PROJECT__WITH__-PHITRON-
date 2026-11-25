from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.musician, name='musician'), # pyright: ignore[reportArgumentType] # pyright: ignore[reportCallIssue] # type: ignore
    
    
]