from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def add_categories(request):
    # return render(request, 'add_categories.html')



    # Backend work ----> categories er form er data save
    # POST request hole:
    if request.method == "POST":
        categories_form = forms.categoriesForm(request.POST)
        if categories_form.is_valid():
            categories_form.save()
            return redirect('add_categories')
    
    # GET request hole:
    else:
       categories_form = forms.categoriesForm()    
       
         
    return render(request, 'add_categories.html', {'form' : categories_form})