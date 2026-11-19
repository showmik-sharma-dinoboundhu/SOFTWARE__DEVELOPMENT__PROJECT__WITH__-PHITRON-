from django.shortcuts import render
from first_app.forms import StudentFrom

# Create your views here.
def home(request):
    std = StudentFrom()
    return render(request, "home.html", {'form' : std});