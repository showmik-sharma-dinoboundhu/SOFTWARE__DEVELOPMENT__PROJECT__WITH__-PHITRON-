from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path("form/", views.form, name='form'),  # type: ignore[attr-defined]
    
]
