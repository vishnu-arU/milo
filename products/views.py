from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('this is response you are seeing')

def message(request):
    return HttpResponse('yep i know you')