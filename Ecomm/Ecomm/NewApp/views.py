from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def news(request):
    return HttpResponse("<h1>This is our latest news </h1>")