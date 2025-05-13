from django.urls import path
from . import views
urlpatterns=[
    # for food
    path('',views.index,name='index'),
    
    # for food id/details
    path('<int:item_id>/',views.details,name='details')


]