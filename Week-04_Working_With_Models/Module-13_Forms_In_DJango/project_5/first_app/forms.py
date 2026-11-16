from django import forms

class contactForm(forms.Form):
    
    # Widget: Field to html input.
    
    
    
    
    name = forms.CharField(label="Full Name : ", initial="Showmik", help_text="Enter you full name within 70 characters", required=False, disabled=False, widget= forms.Textarea(attrs={"id" : "Text_Area", "class": "class1 class2", 'placeholder': "Enter Your Name"}))
    
    # Files Uploads- PDF to everything:
    file = forms.FileField()
    
    
    
    
    email = forms.EmailField(label="User Email")
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.DateField()
    appointment = forms.DateTimeField()
    
    
    
    # Char converted in number or any thing with widget:
    age_usnig_char = forms.CharField(widget=forms.NumberInput)
    birthday_usnig_char = forms.CharField(widget=forms.DateInput(attrs={"type" : "date"}))
    appointment_usnig_char = forms.CharField(widget=forms.DateInput(attrs={"type" : "datetime-local"}))
    
    
    
    
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
