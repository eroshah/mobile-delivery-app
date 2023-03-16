from django.urls import path
from . import views

urlpatterns = [
    path('buy-food',views.StoreView.as_view(),name = 'buyfood'),
    path('one-store/<int:pk>',views.StoreItemView.as_view(),name = 'onestore'),
    path('store-info/<int:pk>',views.StoreInfoView.as_view(),name = 'storeinfo'),





]
