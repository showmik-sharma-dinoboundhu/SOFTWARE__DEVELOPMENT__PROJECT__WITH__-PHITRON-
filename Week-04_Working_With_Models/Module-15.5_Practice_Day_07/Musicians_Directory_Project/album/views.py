from django.shortcuts import render
from . import forms

# Create your views here.
def album(request):
    # return render(request, 'album.html')
    
    album_form = forms.albumForm()
    return render (request, 'album.html', {"form" : album_form})
