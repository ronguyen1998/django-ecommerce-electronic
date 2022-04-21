from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from core.models import Product, Category

# Create your views here.

class HomeView(View):
    def get(self, request):
        list_product = Product.objects.all()
        data_category = Product.objects.filter(category=ca)

        context = {
            "list_product":list_product,
            
        }
        return render(request, 'home/index.html', context)

    def post(self, request):
        pass