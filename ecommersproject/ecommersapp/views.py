from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category,product
# Create your views here.
def index(request):
    return render(request,'base.html')

def allProdCat(request,c_slug=None):
    c_page=None
    Product=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,c_slug=None)
        Product=product.objects.all().filter(category=c_page,available=True)
    else:
        Product=product.objects.all().filter(available=True)
    return render(request,"category.html",{'category':c_page,'product':Product})