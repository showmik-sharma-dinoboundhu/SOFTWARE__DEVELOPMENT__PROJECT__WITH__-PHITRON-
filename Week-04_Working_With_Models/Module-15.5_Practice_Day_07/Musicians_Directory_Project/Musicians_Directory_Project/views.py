from django.shortcuts import render
from album.models import album

def home(request):
    # return render(request, 'home.html')
    
    
    # frontend work:
    data = album.objects.all()
    print(data)
    return render(request, 'home.html', {"data" : data})