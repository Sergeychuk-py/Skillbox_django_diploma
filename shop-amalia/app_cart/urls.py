from django.urls import path

from .views import *

app_name = "cart"

urlpatterns = [
    path("add-product/", add_product_in_cart, name="add_product"),
    path("update-cart/", update_cart_view, name="update_cart"),
    path("update-product-amount/", update_product_amount, name="update_product_amount"),
    path("remove-product/", remove_product, name="remove_product"),
    path("", CartView.as_view(), name="cart"),
]
