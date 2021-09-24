from django.shortcuts import render
from .models import News

# Create your views here.

def news(request):
    obj = News.objects.get(id=1)
    context = {
        "data":obj
    }
    return render(request, 'news.html' , context)      

def home(request):
    context = {"name":"Farooq Abbas","id":15143}
    return render(request, 'home.html',context)

def contact(request):
    return render(request, 'contact.html')   