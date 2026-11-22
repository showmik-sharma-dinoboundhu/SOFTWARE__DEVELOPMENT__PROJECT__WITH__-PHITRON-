from django.shortcuts import render
from .import forms

# Create your views here.
def add_author(request):
    author_form = forms.authorForm()
    return render(request, 'add_author.html', {'form' : author_form})