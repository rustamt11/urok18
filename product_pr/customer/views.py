from django.shortcuts import render
from adminside.models import Product

def index(request):
    products = Product.objects.filter(status='available')
    return render(request, 'customer/index.html', {'products': products})
