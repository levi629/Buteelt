"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from ecommerce import settings
from django.conf.urls.static import static
# from django.conf import settings
from shop_app.views import (
    index, register, dashboard, order_complete, place_order,
    product_detail, search_result, store, signin
)
from carts.views import (
    cart, add_cart,remove_cart_item, reduce_cart_item
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('signin/', signin, name='signin'),
    path('card', cart, name='cart'),
    path('card/add/<int:product_id>/', add_cart, name='add_cart'),
    path('card/remove/<int:product_id>/', remove_cart_item, name='remove_cart_item'),
    path('card/reduce/<int:product_id>/', reduce_cart_item, name='reduce_cart_item'),
    path('<slug:category_slug>', store, name='store'),
    path('search/<slug:category_slug>', store, name='store'),
    path('<slug:category_slug>/<slug:product_slug>', product_detail, name='product_detail'),
    path('place-order/', place_order, name='place_order'),
    path('order-complete/', order_complete, name='order_complete'),
    path('dashboard/', dashboard, name='dashboard'),    
    path('search/', search_result, name='search_result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
