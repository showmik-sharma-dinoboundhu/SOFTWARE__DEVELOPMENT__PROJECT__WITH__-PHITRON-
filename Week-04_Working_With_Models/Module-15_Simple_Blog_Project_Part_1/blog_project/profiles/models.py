from django.db import models

# Create your models here.
class profiles(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    