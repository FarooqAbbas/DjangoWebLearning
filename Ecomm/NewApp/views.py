from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def news(request):
    context = {"list":['python','java','C++','C#']}
    return render(request , 'news.html',context)

def home(request):
    context = {"name":"Farooq Abbas","id":15143}
    return render(request , 'home.html',context)

def contact(request):
    return render(request ,'contact.html')   