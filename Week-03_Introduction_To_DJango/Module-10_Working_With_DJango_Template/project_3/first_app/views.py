from django.shortcuts import render

# Create your views here.

def home(request):
    d = {'Author' : 'Showmik', 'Age' : 22, 'List' : [1,2,3,4]}
    return render(request,'home.html', d)