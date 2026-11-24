from django.shortcuts import render, redirect
from . import forms
from . import models

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
 
 
 
def edit_posts(request, id):
    # edit things:
    post = models.posts.objects.get(pk = id) #pk = pirmary key
    # print(post.title)
    posts_form = forms.postsForm(instance=post)
    
    
    
    # First when post was writen:
    # return render (request, 'add_posts.html')


    # Backend work ----> Posts er form er data save
    # POST request hole:
    if request.method == "POST":
        posts_form = forms.postsForm(request.POST, instance=post)
        if posts_form.is_valid():
            posts_form.save()
            return redirect('homepage')
        
    # get request hole:
    # else:
    #     posts_form = forms.postsForm()
        
    return render (request, 'add_posts.html', {'form' : posts_form})
 
 

def delete_post(request,id):
        post = models.posts.objects.get(pk = id) #pk = pirmary key
        post.delete()
        return redirect('homepage')
