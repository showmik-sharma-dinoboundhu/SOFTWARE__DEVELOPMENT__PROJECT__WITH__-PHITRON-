from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, './html_temp/index.html')

def about(request):
    name = ""
    email = ""
    select = ""
    if(request.method) == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        select = request.POST.get("select")
        return render(request, './html_temp/about.html', {"name" : name, "email" : email, "select" : select})
    else:
        return render(request, './html_temp/about.html')

def form(request):
    return render(request, './html_temp/form.html')

