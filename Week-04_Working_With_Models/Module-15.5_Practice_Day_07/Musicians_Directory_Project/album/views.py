from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def album(request):
    # nortmal views.py
    # return render(request, 'album.html')
    
    
    #forms show in site: 
    # album_form = forms.albumForm()
    # return render (request, 'album.html', {"form" : album_form})
    
    
    # # Backend work ----> Album er form er data save
    # GET or POST forms:
    
    # POST request hole:
    if request.method == "POST":
        album_form = forms.albumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('album')
        
    # else request hole:
    else:
        album_form = forms.albumForm()
    
        
        
    return render(request, 'album.html', {"form" : album_form})
