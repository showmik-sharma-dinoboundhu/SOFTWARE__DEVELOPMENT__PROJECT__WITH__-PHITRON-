from django.urls import path
from typing import Any, cast
from .import views

urlpatterns = [
    path('', views.home, name = "homepage"),
    path('delete/<int:roll>', cast(Any, views.delete_student), name = "delete_student"),
    
]
