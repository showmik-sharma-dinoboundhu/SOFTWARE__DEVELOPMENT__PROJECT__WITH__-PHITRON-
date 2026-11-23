from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def add_posts(request):
    # return render (request, 'add_posts.html')


    # Backend work ----> Posts er form er data save
    # POST request hole:
    if request.method == "POST":
        posts_form = forms.postsForm(request.POST)
        if posts_form.is_valid():
            posts_form.save()
            return redirect('add_posts')
        
    # get request hole:
    else:
        posts_form = forms.postsForm()
        
    return render (request, 'add_posts.html', {'form' : posts_form})
 