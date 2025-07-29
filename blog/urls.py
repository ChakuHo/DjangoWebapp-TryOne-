from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blog'),
    path('<slug:slug>/', views.details1, name='details1'),
]
