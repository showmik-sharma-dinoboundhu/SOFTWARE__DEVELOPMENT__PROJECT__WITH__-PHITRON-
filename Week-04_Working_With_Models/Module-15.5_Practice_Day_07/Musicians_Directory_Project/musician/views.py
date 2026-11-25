from django.shortcuts import render
from . import forms

# Create your views here.
def musician(request):
    # return render(request, 'musician.html')
    
    musician_form = forms.musicianForm()
    return render (request, 'musician.html', {"form" : musician_form})