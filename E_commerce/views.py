from django.shortcuts import get_object_or_404, render
from .models import Customer, Product

def home(request):
    return render(request, 'E_commerce/home.html')

# View for listing products
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'E_commerce/product_list.html', context)

# View for product details
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'E_commerce/product_detail.html', context)

# View for listing customers
def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'E_commerce/customer_list.html', context)

# View for customer details
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    context = {
        'customer': customer
    }
    return render(request, 'E_commerce/customer_detail.html', context)
