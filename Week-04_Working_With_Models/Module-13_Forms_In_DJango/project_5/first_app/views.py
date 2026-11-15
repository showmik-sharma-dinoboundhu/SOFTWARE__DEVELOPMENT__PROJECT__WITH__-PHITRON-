from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, './html_temp/index.html')

def about(request):
    return render(request, './html_temp/about.html')

def form(request):
    if(request.method) == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        return render(request, './html_temp/form.html', {"name" : name, "email" : email})
    else:
        return render(request, './html_temp/form.html')

