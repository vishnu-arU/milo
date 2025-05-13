from django.shortcuts import render
from django.http import HttpResponse
from.models import Products
from django.template import loader
# Create your views here.
def index(request):
    product_list=Products.objects.all()
    template=loader.get_template('products/index.html')
    context={
        

    }
    return HttpResponse(template.render(context,request))

def message(request):
    return HttpResponse('yep i know you')