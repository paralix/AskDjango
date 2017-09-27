from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def mysum(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.split('/')))
    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse("안녕하세요? {}이고, {}살 입니다".format(name, age))
