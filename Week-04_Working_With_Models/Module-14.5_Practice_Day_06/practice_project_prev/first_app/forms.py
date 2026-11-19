from django import forms

class studentForm(forms.Form):
    name = forms.CharField()
    roll = forms.IntegerField()
    father_name = forms.CharField()
    mother_name = forms.CharField()