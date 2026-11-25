from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.album, name='album'),  # type: ignore[call-overload, arg-type]
]