from .models import *
from  carts.models import Cart, CartItem
from  carts.views import _cart_id

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            cart_count += item.quantity
    except Cart.DoesNotExist:
        cart_count = 0
    return dict(cart_count=cart_count)