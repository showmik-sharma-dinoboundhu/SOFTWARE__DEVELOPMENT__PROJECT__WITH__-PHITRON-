from django import forms
from . models import musician

class musicianForm(forms.ModelForm):
    class Meta:
        model = musician
        fields = '__all__'