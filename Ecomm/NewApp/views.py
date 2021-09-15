from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def news(request):
    return render(request , 'news.html',)

def home(request):
    return render(request , 'home.html')

def contact(request):
    return render(request ,'contact.html')   