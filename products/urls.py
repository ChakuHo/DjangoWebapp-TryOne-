from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name="product"),
    path('<slug:slug>/', views.products_details1, name="products_details1"),
]
