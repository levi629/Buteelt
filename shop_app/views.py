from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Product
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
    ser = request.GET.get("q", "").strip()
    cat = Category.objects.all()
    if ser:
        products = Product.objects.filter(product_name__icontains=ser, is_available=True).order_by('id')
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3) 
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    
    return render(request , "search-result.html", {'result' : paged_products, "count": len(products)})

def signin(request):
    return render(request , "signin.html")

def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug != "None":
        categories = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')

    product_count = products.count()
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    return render(request , "store.html", {'categories' : categories, 'result' : paged_products, "count": product_count})


