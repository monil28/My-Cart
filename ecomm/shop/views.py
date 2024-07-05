from django.shortcuts import render
from . models import Product
from math import ceil
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Shop Home Page')
    products = Product.objects.all()
    n=len(products)
    slides = n//4 + (ceil(n/4)-n//4)
    context = {
        'products': products,
        'slides': slides,
        'range': range(1, slides)
    }
    return render(request, 'shop/index.html', context)

def about(request):
    return render(request, 'shop/about.html')
