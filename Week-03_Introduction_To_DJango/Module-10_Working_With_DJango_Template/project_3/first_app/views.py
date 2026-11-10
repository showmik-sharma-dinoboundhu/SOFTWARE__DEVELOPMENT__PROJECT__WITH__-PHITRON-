from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    d = {'Author' : 'Showmik', 'Age' : 16, 'List1' : ['Python', 'is', 'Best', 'full-stop'], 
         'Birthdate' : datetime.datetime.now(), 'List' : [1,2,3,4],
         'val' : '',
         'Courses' : [
        {
            'id' : 1,
            'name' : 'Python',
            'fee' : 6500,
        },
        {
            'id' : 2,
            'name' : 'DJango',
            'fee' : 6500,
        },
        {
            'id' : 3,
            'name' : 'CPP',
            'fee' : 6500,
        },
    ]}
    return render(request,'home.html', d)