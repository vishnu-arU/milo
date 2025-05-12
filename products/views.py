from django.shortcuts import render
from django.http import HttpResponse
from.models import Products
# Create your views here.
def index(request):
    product_list=Products.objects.all()
    return HttpResponse(product_list)

def message(request):
    return HttpResponse('yep i know you')