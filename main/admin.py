from django.contrib import admin
from .models import Product, Image, Header

# Register your models here.
class HeaderAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'image']

class ImageAdmin(admin.StackedInline):
    model = Image
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    fields = ['title', 'desc', 'price', 'slug']
    prepopulated_fields = {"slug": ('title',)}
    inlines = [ImageAdmin]

admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
admin.site.register(Header, HeaderAdmin)