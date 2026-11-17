from django import forms

class contactForm(forms.Form):
    
    # # Widget: Field to html input.    
    # name = forms.CharField(label="Full Name : ", initial="Showmik", help_text="Enter you full name within 70 characters", required=False, disabled=False, widget= forms.Textarea(attrs={"id" : "Text_Area", "class": "class1 class2", 'placeholder': "Enter Your Name"}))
    
    
    # # Files Uploads- PDF to everything:
    # file = forms.FileField()
    
    
    
    
    # email = forms.EmailField(label="User Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    # birthday = forms.DateField()
    # appointment = forms.DateTimeField()
    
    
    
    
    
    
    
    
    # # Char converted in number or any thing with widget:
    # age_usnig_char = forms.CharField(widget=forms.NumberInput)
    # birthday_usnig_char = forms.CharField(widget=forms.DateInput(attrs={"type" : "date"}))
    # appointment_usnig_char = forms.CharField(widget=forms.DateInput(attrs={"type" : "datetime-local"}))
    
    
    
    
    # Choiches:
    CHOICES = [("S", "Small"), ("M", "Medium"), ("L", "Large")]
    size = forms.ChoiceField(choices=CHOICES)
    
    # Choiches using Radio Select with char field and widget:
    size_radio_select_char = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    
    # Multiple variable user choose:
    MEAL = [("P", "Pepperoni"), ("M", "Mashroom"), ("Mtn", "Mutton")]
    pizza = forms.MultipleChoiceField(choices=MEAL)
    
    # Multiple choice using char field widget:
    pizza_widget_multple = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)




class studentData(forms.Form):
    #  Char widget mail and Name:
    name = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.EmailInput)
    
    def clean_name(self):
        valnmae = self.cleaned_data["name"]
        if len(valnmae) < 10:
            raise forms.ValidationError("Enter a name with at least 10 characters")
        return valnmae
    
    def cleaa_email(self):
        valemail = self.cleaned_data['email']
        if '.com' not in valemail:
            raise forms.ValidationError("Your mail must not ok")
        return valemail
    
    
    # Shortcut:
    def clean(self):
        cleaned_data = super().clean()
        valname =self.cleaned_data['name']
        valnemail =self.cleaned_data['email']
        