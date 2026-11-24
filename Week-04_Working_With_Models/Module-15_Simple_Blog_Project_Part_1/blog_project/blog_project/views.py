from django.shortcuts import render
from posts.models import posts

def home(request):
    # return render(request, 'home.html')
    
    
    # Frontend work:
    data = posts.objects.all()
    # for post in data:
    #     print(post.title)
    #     print(post.categories.all())

    print(data)
    return render(request, 'home.html', {'data' : data})
