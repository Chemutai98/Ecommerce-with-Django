from django.urls import path
from . import views

app_name = 'E_commerce'

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('customer_list/', views.customer_list, name='customer_list'),
    path('customer_detail/<int:pk>/', views.customer_detail, name='customer_detail'),  # Added trailing slash
]
