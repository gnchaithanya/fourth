from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def chaithu(request):
    return HttpResponse('<h1><marquee >Hii chaithu, How are you.....<marquee></h1>')

def divya(request):
    return HttpResponse('<i><h1><marquee>Hii Divyasree, How are you......</marquee></h1></i>')