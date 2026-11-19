from django import forms
from first_app.models import StudentModel

class StudentFrom(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = "__all__"
        # fields = ['name', 'roll']
        
        # field & exclude same:
        # exclude = "__all__"
        
        labels = {
            "name" : "Student Name",
            "Roll" : "Student Roll"
        }
        
        widgets = {
            "name" : forms.TextInput(),
        }
        
        help_texts = {
            "name" : "Write Your Full-Name"
        }
        
        error_messages = {
            "name" : {"Required" : "Your Name is Required"}
        }