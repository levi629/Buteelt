from django.db import models
from django.db.models.fields import SlugField
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='media/categories', blank=True)
    def __str__ (self):
        return self.category_name
    class Meta:
        db_table='tbl_categories'
    def get_url(self):
        return reverse('store', args=[self.slug])

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='media/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    def __str__ (self):
         return self.product_name
    class Meta:
        db_table='tbl_products'
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])


class imageGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/products',)
    
    def __str__(self):
        return self.product.product_name
    
class ProductImages(models.Model):
    product = models.ForeignKey(Product,
    on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products',max_length=255)
    def __str__(self):
        return self.product.product_name