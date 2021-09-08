from django.urls import path
from django.urls.resolvers import URLPattern
from .views import news

urlpatterns ={
    path('news/',news,name='News')
}