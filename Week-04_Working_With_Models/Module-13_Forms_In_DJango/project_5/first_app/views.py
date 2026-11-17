from django.shortcuts import render
from .forms import contactForm
from .forms import studentData

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


# Normal Approch:
# def django_form(request):
#     form = contactForm(request.POST)
#     if form.is_valid():
#         print(form.cleaned_data)
#     return render(request,'./html_temp/django_form.html', {"form" : form}) # type: ignore


# Best Approch:
# def django_form(request):
#     form = contactForm()
#     if(request.method == "POST"):
#         form = contactForm(request.POST, request.FILES)
#         if form.is_valid():
#             # file = form.cleaned_data['file']
#             # with open("./first_app/upload/" + file.name, "wb+") as destination:
#             #     for chunks in file.chunks():
#             #         print(chunks)
#             print(form.cleaned_data)
#         return render(request, './html_temp/django_form.html', {"form": form})
    
#     else:
#         form = contactForm()
    
#     return render(request, './html_temp/django_form.html', {"form": form})




# StudentData:
def django_form(request):
    form = studentData()
    if(request.method == "POST"):
        form = studentData(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
    
    return render(request, "./html_temp/django_form.html", {"form" : form})


