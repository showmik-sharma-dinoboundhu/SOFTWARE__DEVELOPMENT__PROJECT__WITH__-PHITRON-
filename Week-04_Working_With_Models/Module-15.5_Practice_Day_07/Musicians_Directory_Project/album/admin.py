from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.album)

def __str__(self):
    return self.name