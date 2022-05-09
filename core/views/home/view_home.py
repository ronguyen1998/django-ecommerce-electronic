from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from core.models import Product, Category

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

class HomeView(View):
    def get(self, request):
        list_product = Product.objects.all()
        # data_category = Product.objects.filter(category=ca)
        list_category = Category.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(list_category, 20)
        try:
            cat = paginator.page(page)
        except PageNotAnInteger:
            cat = paginator.page(1)
        except EmptyPage:
            cat = paginator.page(paginator.num_pages)
        
        context = {
            "list_product":list_product,
            'categories': cat
            
        }
        return render(request, 'home/index.html', context)

    def post(self, request):
        pass