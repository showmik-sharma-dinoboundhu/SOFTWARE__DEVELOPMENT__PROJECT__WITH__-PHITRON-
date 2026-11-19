from django import forms
from first_app.models import StudentModel

class StudentFrom(forms.ModelForm):
    class Meta:
        model = StudentModel
        # fields = "__all__"
        fields = ['name', 'roll']