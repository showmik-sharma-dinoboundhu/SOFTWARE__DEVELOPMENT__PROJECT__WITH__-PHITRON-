from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def add_profiles(requeest):
    # return render (requeest, 'add_profiles')
    
    
    # Backend work ----> Author er form er data save
        # POST request hole:
        if requeest.method == "POST":
            profiles_form = forms.profilesForm(requeest.POST)
            if profiles_form.is_valid():
                profiles_form.save()
                return redirect('add_profiles')
        
        # GET request hole:
        else:
           profiles_form = forms.profilesForm()    
           
             
        return render(requeest, 'add_profiles.html', {'form' : profiles_form})