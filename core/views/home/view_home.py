from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from core.models import Product, Category

# Create your views here.

class HomeView(View):
    def get(self, request):
        list_product = Product.objects.all()
        

        context = {
            "list_product":list_product,
            
        }
        return render(request, 'home/index.html', context)

    def post(self, request):
        pass