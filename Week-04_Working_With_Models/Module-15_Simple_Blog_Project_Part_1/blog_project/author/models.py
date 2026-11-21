from django.db import models

# Create your models here.
class author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    phone_num = models.CharField(max_length=11)
    
    
    