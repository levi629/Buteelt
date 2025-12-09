from django.contrib import admin
from .models import Category, Product, imageGallery, ProductImages

admin.site.register(ProductImages)

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}

class ProductImageLine(admin.StackedInline):
    model = imageGallery
    extra = 3
    
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    inlines =[
        ProductImageLine
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
