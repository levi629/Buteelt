from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Product
from django.db.models import Q
import sqlite3
# Create your views here.
def index(request):
    cat = Category.objects.all()
    prod = Product.objects.all()[:8]
    return render(request , "index.html", {'categories' : cat, 'products' : prod, "count": len(prod)})


def dashboard(request):
    return render(request , "dashboard.html")
def order_complete(request):
    return render(request , "order_complete.html")
def place_order(request):
    return render(request , "place-order.html")
def product_detail(request, category_slug, product_slug):
    pro = Product.objects.get(slug=product_slug, category__slug=category_slug)
    return render(request , "product-detail.html", {'product': pro})
def register(request):
    return render(request , "register.html")
# def search_result(request):
#     ser = request.GET.get("q", "").strip()
#     # prod = Product.objects.none()
#     prod = Product.objects.all().filter(product_name__icontains=ser)
#     return render(request , "search-result.html", {'result' : prod, "count": len(prod)})

def search_result(request):
    ser = request.GET.get("keyword", "").strip()
    products = Product.objects.filter(is_available=True)
    
    if ser:
        products = products.filter(
            Q(product_name__icontains=ser) | Q(description__icontains=ser)
        ).order_by('id')
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3) 
    page = request.GET.get('page')  
    paged_products = paginator.get_page(page)
    
    return render(request , "store.html", {'result' : paged_products, "count": len(products), 'keyword': ser})

def signin(request):
    return render(request , "signin.html")

def store(request, category_slug=None):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    products = Product.objects.filter(is_available=True).order_by('id')
    if category_slug != "None":
        categories = Category.objects.get(slug=category_slug)
        products = products.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price and max_price != '2000':
        products = products.filter(price__lte=max_price)
        
    product_count = products.count()
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    return render(request , "store.html", {'result' : paged_products, "count": product_count})


