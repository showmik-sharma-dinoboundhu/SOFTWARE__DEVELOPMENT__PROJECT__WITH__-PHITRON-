from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def musician(request):
    # return render(request, 'musician.html')
    
    # musician_form = forms.musicianForm()
    # return render (request, 'musician.html', {"form" : musician_form})



# POST request hole:
    if request.method == "POST":
        album_form = forms.musicianForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('album')
        
    # else request hole:
    else:
        album_form = forms.musicianForm()
    
        
        
    return render(request, 'album.html', {"form" : album_form})
