from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class BlogsCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField(default=0)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(BlogsCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)  # upload_to='blogs/' means images go inside MEDIA_ROOT/blogs/

        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # auto-generate slug from the blog title
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
