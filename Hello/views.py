from django.shortcuts import render
from django.http import HttpResponse  #2. after installing app in settings, in views import HttpResponse
from django import forms
from .forms import studentform
from .models import students

# Create your views here.
form = studentform()
my_dict ={"insert_me": "Its lowest ...","sr": "star dust","n": 300, 'form': form}

def index(request):       #2.1 create a function by name index with request as default
    return HttpResponse("<h1>I started learning Django and its fun")
def Hello(request):       #5.0 creating a func Hello
    #return HttpResponse("<h2> I am coming from the application urls.py file</h2>")
    if request.method == "POST":  # 10.3
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = studentform()

    return render(request,'Hello/Home.html',context =my_dict)   #  in template folder Hello folder is present, inside Hello folder Home.html page is present

def list_view(request):             # to read the data present in the table
    #dictionary for initial data with
    # field names as keys
    context ={}   # empty dictionary

    # add the dictionary during initialization
    context["dataset"] = students.objects.all()   # dataset is key, students.objects it read the objects of student class in model it gives an array as output
    return render(request, "Hello/list_view.html",context)  # INSIDE Hello we are creating list_view.html

