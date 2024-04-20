from django.shortcuts import render
from django.http import HttpResponse
from .models import *



# Create your views here.
def index(request):
    iid=item.objects.all()
    sdata=slider.objects.all().order_by('id')[0:5]
    itdata=itemcategory.objects.all().order_by('id')[0:3]
    md={'idata':iid,'sdata':sdata,'itdata':itdata}
    return render(request,"base.html",md)