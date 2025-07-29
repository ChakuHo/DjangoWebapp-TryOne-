from django.shortcuts import render, get_object_or_404
from . models import Blog

# Create your views here.
def blogs(request):
    all_blogs = Blog.objects.filter(status=True).order_by('created_at')
    return render(request, 'blogs/blogs1.html', {'blogs': all_blogs})

def details1(request, slug):
    blog = get_object_or_404(Blog, slug=slug, status=True)
    return render(request, 'blogs/details1.html', {'blog': blog})