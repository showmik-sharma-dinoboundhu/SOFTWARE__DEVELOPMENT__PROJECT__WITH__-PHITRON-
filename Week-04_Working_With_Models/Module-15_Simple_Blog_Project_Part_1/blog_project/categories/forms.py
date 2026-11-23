from django import forms
from .models import categories

class categoriesForm(forms.ModelForm):
    class Meta:
        model = categories
        fields = '__all__'
        