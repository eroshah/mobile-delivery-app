from django.urls import path
from . import views

urlpatterns = [
    path('',views.CartView.as_view(),name = 'cart'),
    path('add-to-cart/<int:pk>',views.AddToCartView.as_view(),name='addtocart'),
]
