from django.shortcuts import render

# Create your views here.


def home(request):
    d = {"Author" : "Showmik Sharma",
         "Age" : 24, 
         "Study" : "NUB",
         "Num" : [10, 20, 30],
         "Fruits" : [ 'Banana', 'Apple', 'Orange', 'Mango'],
         "Animal" : ['cat', 'dog', 'cow', 'goat'],       
         "Courses" : [
             {
                "id" : 2002,
                "Name" : "Dinoboundhu",
                "Study" : "CSE", 
                "Profesion": "Backend Developer",
             },
             {
                "id" : 4008,
                "Name" : "Devdut",
                "Study" : "Machanical", 
                "Profesion": "Jr Site Engineer",
                
             },
             {
                "id" : 60010,
                "Name" : "Dingon",
                "Study" : "DTNT", 
                "Profesion": "Network Engineer",
             },
             {
                "id" : 80012,
                "Name" : "Nittanondo",
                "Study" : "Electrical", 
                "Profesion": "Walton Industrial",
             }
         ]
        }
    return render(request, "html/home.html", d)