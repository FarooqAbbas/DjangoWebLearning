from django.urls import path
from .views import news,home,contact

urlpatterns ={
    path('news/', news, name='News'),
    path('', home, name='Home'),
    path('contact/', contact, name='Contact')
}