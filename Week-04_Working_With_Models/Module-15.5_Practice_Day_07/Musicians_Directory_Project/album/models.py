from django.db import models
from musician.models import musician

# Create your models here.
class album(models.Model):
    album_name = models.CharField(max_length=50)
    musician = models.ForeignKey(musician,on_delete=models.CASCADE)
    album_relase_date = models.DateField()
    rating = models.CharField(max_length=5)
    
    
    def __str__(self):
        return self.album_name
    
    
    

