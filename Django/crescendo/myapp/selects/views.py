from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def selects(request) :
    return render(request, 'selects/selects.html')
