from django.urls import path
from .views import *

urlpatterns = [
    path('',demo),
    path("showproduct/", show_product),
    path("addcategory/",post_category),
    path('addproduct/',post_product),
    path('showcategory/',show_category),
    path('delete_category/<int:category_id>/',delete_category),
    path('update_category/<int:category_id>/',update_category),
    path('update_product/<int:product_id>/',update_product),
    path('delete_product/<int:product_id>/',delete_product),
]


