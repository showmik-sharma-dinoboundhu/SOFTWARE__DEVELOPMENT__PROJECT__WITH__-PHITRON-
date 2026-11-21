from django.db import models
from categories.models import categories
from author.models import author

# Create your models here.
class posts(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    
    catagories = models.ManyToManyField(categories)  # ekta post multiple categories er modde thakte pare abr ekta catagories te multiple post thakte pare
    
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    
    
    # title show
    def __str__(self):
        return self.title