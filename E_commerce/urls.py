from django.urls import path
from . import views

app_name = 'E_commerce'

urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.product_list, name='product_list'),
    path('products<int:pk>/', views.product_detail, name='product_detail'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer_detail/<int:pk>/', views.customer_detail, name='customer_detail'),
]
