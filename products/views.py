from django.shortcuts import render, get_object_or_404
from . models import Product

# Create your views here.
def product(request):
    products = Product.objects.all()
    return render(request, 'products/products1.html', {'products': products})

def products_details1(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/products_details1.html', {'product': product})