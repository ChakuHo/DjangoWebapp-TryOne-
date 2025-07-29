from django.shortcuts import render
from products.models import Product
from blog.models import Blog
from pages.models import Page

def home(request):
    products = Product.objects.all()
    blogs = Blog.objects.all()
    pages = Page.objects.all()
    return render(request, 'home/home1.html', {
        'products': products,
        'blogs': blogs,
        'page': pages,
    })