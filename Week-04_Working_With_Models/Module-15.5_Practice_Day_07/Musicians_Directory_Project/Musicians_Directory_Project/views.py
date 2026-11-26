from django.shortcuts import render
from album.models import album

def home(request):
    # return render(request, 'home.html')
    
    
    # frontend work:
    data = album.objects.all()
    print(data)
    
    # comma diye jonto instrument ache tader k alada alada kore alada button e rakhar jonno code:
    for i in data:
        i.instruments = i.musician.instrument_type.split(',') # type: ignore
    
    
    return render(request, 'home.html', {"data" : data})