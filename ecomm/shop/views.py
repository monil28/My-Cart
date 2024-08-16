from django.shortcuts import render
from . models import Contact, Product
from math import ceil
# from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('Shop Home Page')
    # products = Product.objects.all()
    # n = len(products)
    # slides = n//4 + (ceil(n/4)-n//4)
    # context = {
    #     'products': products,
    #     'slides': slides,
    #     'range': range(1, slides)
    # }

    # allProds = [[products, range(1, slides)], [products, range(1, slides)]]
    allProds = []
    catProd = Product.objects.values('category', 'id')
    categories = {item['category'] for item in catProd}
    for cat in categories:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        slides = n//4 + (ceil(n/4)-n//4)
        allProds.append([prod, range(1, slides)])
    # print(allProds)
    context = {
        'allProds': allProds
    }
    return render(request, 'shop/index.html', context)


def about(request):
    return render(request, 'shop/about.html')


def productview(request, product_id):
    product = Product.objects.filter(id=product_id)
    return render(request, 'shop/productview.html', {'product': product[0]})


def checkout(request):
    return render(request, 'shop/checkout.html')


def contact(request):
    if request.method == "POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')
