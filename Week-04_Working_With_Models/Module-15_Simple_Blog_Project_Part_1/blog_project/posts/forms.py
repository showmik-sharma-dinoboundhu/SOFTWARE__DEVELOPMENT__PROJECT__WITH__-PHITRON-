from django import forms
from . models import posts

class postsForm(forms.ModelForm):
    class Meta:
        model = posts
        fields = '__all__'
        