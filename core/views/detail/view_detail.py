from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404 
from django.views import View
from core.models import Product
# Create your views here.

def DetailProductView(request, id_product):
    
        detail_product = Product.objects.get(pk=id_product)
        return render(request, 'detail/detail_product.html',{'detail_product':detail_product})
    
