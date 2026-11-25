from django.db import models

# Create your models here.
class musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=11)
    instrument_type = models.TextField()
    
    
    def __str__(self):
        return f"self.first_name, self.last_name"