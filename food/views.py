from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
# Create your views here.
def index(request):
# old codes are in # 
    item_list=Item.objects.all()
    # template=loader.get_template('food/index.html')
    context={
        'item_list':item_list,

    }
    return render(request,'food/index.html',context)


    # return HttpResponse(template.render(context,request))




def details(request,item_id):
    return HttpResponse("this is the id /no: %s" % item_id)