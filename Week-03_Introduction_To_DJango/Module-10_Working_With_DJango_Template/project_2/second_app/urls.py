from django.urls import path
# from second_app.views import home
# from second_app import views
from .import views

urlpatterns = [
    path("", views.home), # type: ignore
]
