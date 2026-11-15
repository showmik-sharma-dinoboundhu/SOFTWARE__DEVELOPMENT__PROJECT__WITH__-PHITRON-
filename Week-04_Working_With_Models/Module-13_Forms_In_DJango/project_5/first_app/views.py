from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, './html_temp/index.html')

def about(request):
    return render(request, './html_temp/about.html')

def form(request):
    return render(request, './html_temp/form.html')

