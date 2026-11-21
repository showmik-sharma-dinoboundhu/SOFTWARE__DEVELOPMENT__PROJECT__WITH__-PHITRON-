from django.db import models
from author.models import author


# Create your models here.
class profiles(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    
    # one to one field:
    author = models.OneToOneField(author, on_delete=models.CASCADE, default=None)


    # Name show
    def __str__(self):
        return self.name