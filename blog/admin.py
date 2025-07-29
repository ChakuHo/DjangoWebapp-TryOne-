from django.contrib import admin
from . models import Blog, BlogsCategory
from django.utils.html import format_html
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(BlogsCategory, CategoryAdmin)

class BlogAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    list_display = ('id', 'title','author', 'short_content', 'category', 'created_at', 'updated_at', 'status', 'show_image')
    list_filter = ('status', 'category')
    search_fields = ('title', 'author', 'content')
    prepopulated_fields = {"slug": ("title",)}  # autocomplete from title

    def short_content(self, obj):
        return ' '.join(obj.content.split()[:6]) + '...'

    def show_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="object-fit: cover; border-radius:50%;" />', obj.image.url)
        return "No Image"
    show_image.short_description = 'Image'

admin.site.register(Blog, BlogAdmin)

