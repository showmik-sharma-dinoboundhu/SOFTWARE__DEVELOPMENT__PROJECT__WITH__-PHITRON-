from django.shortcuts import render,redirect
from . import forms, models

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
                
            # GET request hole:
            else:
                album_form = forms.albumForm()
            
                
            return render(request, 'album.html', {"form" : album_form})
        


def edit_album(request, id):
    # edit thing:
    albums = models.album.objects.get(pk = id)
    album_form = forms.albumForm(instance=albums)
    
    
    if request.method == "POST":
        album_form = forms.albumForm(request.POST, instance=albums)
        if album_form.is_valid():                           album_form.save()
        return redirect('homepage')
                   
                    
        # # GET request hole:
            # etar dorkar nai
                # else:
                # album_form = forms.albumForm()
                    
                    
    return render(request, 'album.html', {"form" : album_form})


def delete_album(request, id):
    # delete things:
    albums = models.album.objects.get(pk = id)
    albums.delete()
    return redirect ("homepage")