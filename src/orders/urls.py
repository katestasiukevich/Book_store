from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path('cart/', views.view_cart, name="view-cart"),
    path('add-item/', views.add_item_to_cart_view, name="add-item-to-cart"),
    path('evaluate/', views.evaluate_cart, name="evaluate-cart"),
    path('create-order/', views.CreateOrderView.as_view(), name="view-order-created"),
]