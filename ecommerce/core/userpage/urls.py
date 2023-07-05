from django.urls import path
from .views import *


urlpatterns = [
    path('',homepage ),
    path('productdetail/<int:product_id>/',productdetail),
    path('products/',product),
    path('contact/',contact),
    path('cart/<int:product_id>', add_to_cart),
    path('mycart/',show_cart_items),
    path('deletecart/<int:cart_id>',delete_cart_items),
    path('order/<int:product_id>/<int:cart_id>',order_form),
    

]
