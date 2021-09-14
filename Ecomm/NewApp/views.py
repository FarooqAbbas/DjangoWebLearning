from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def news(request):
    return render(request , 'home.html')

def home(request):
    return HttpResponse("<h1>This is our home page </h1>")

def contact(request):
    return HttpResponse("<h1>This is contact us page <h1>")    