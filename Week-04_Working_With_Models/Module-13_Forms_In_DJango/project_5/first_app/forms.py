from django import forms
from django.core import validators


class contactForm(forms.Form):
        pass
    
    # # Widget: Field to html input.    
    # name = forms.CharField(label="Full Name : ", initial="Showmik", help_text="Enter you full name within 70 characters", required=False, disabled=False, widget= forms.Textarea(attrs={"id" : "Text_Area", "class": "class1 class2", 'placeholder': "Enter Your Name"}))
    
    
#     # # Files Uploads- PDF to everything:
#     # file = forms.FileField()
    
    
    
    
#     # email = forms.EmailField(label="User Email")
#     # age = forms.IntegerField()
#     # weight = forms.FloatField()
#     # balance = forms.DecimalField()
#     # check = forms.BooleanField()
#     # birthday = forms.DateField()
#     # appointment = forms.DateTimeField()
    
    
    
    
    
    
    
    
#     # # Char converted in number or any thing with widget:
#     # age_usnig_char = forms.CharField(widget=forms.NumberInput)
#     # birthday_usnig_char = forms.CharField(widget=forms.DateInput(attrs={"type" : "date"}))
#     # appointment_usnig_char = forms.CharField(widget=forms.DateInput(attrs={"type" : "datetime-local"}))
    
    
    
    
#     # Choiches:
#     CHOICES = [("S", "Small"), ("M", "Medium"), ("L", "Large")]
#     size = forms.ChoiceField(choices=CHOICES)
    
#     # Choiches using Radio Select with char field and widget:
#     size_radio_select_char = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    
#     # Multiple variable user choose:
#     MEAL = [("P", "Pepperoni"), ("M", "Mashroom"), ("Mtn", "Mutton")]
#     pizza = forms.MultipleChoiceField(choices=MEAL)
    
#     # Multiple choice using char field widget:
#     pizza_widget_multple = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)




# class studentData(forms.Form):
#     #  Char widget mail and Name:
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    
#     def clean_name(self):
#         valnmae = self.cleaned_data["name"]
#         if len(valnmae) < 10:
#             raise forms.ValidationError("Enter a name with at least 10 characters")
#         return valnmae
    
#     def cleaa_email(self):
#         valemail = self.cleaned_data['email']
#         if '.com' not in valemail:
#             raise forms.ValidationError("Your mail must not ok")
#         return valemail
    
    
#     # Shortcut:
#     def clean(self):
#         cleaned_data = super().clean()
#         valname =self.cleaned_data['name']
#         valnemail =self.cleaned_data['email']
#         return cleaned_data
        
        
class studentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MaxLengthValidator(10, message="Enter a name with only between 10 characters")])
    Name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message="Enter a name with minimum 10 characters")])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid email with @ and full stop(.)")])
    age = forms.IntegerField(widget=forms.NumberInput, validators=[validators.MaxValueValidator(34, message="Age must be max 34"), validators.MinValueValidator(24, message="Age must be atleast 24")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=["pdf","png", "jpg", "jpeg"], message="File extension must be ended with .pdf")])