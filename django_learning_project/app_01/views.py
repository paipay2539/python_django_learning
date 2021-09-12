from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello1(request):
    return HttpResponse('Hello World1')

def hello2_1(request, id):
    text = "Hello World2_1 " + str(id)
    return HttpResponse(text)

def hello2_2(request, year, slug):
    text = "Hello World2_2 " + str(year)+ " " + str(slug)
    return HttpResponse(text)

def hello3(request, year, slug):
    text = "Hello World3 " + str(year)+ " " + str(slug)
    return HttpResponse(text)