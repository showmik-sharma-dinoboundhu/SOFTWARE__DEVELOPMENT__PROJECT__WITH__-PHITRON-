
from . import views
from django.urls import path

urlpatterns = [
    
    path('', views.index, name = 'home'),
    path('about/page/<int:id>', views.about, name = 'about')
   
]
