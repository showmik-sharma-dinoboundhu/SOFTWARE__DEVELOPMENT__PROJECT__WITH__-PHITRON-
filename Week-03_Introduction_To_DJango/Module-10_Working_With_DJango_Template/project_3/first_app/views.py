from django.shortcuts import render

# Create your views here.

def home(request):
    d = {'Author' : 'Showmik', 'Age' : 16, 'List' : [1,2,3,4], 'Courses' : [
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