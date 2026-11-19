from django.shortcuts import render
from first_app.forms import StudentFrom

# Create your views here.
def home(request):
    if request.method == "POST":
        form = StudentFrom(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentFrom()
    return render(request, "home.html", {'form' : form});