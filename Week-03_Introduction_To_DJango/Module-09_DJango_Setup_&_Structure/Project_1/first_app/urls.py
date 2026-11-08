from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("courses/", views.courses), # type: ignore
    

]
