from django.shortcuts import render
from products.models import Product

def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "", {"products": products})
    ## here "" You need to put the page that is it inside the Products.models