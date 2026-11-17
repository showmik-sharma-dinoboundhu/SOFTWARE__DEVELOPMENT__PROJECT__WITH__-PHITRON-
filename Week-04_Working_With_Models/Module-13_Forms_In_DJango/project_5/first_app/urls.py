from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path("form/", views.form, name='form'),  # type: ignore[attr-defined]
    path("django_form/", views.django_form, name='django_form'),  # type: ignore[attr-defined]
    path("password_validation/", views.passwordValidation, name='password_validation'), # type: ignore
    
]
