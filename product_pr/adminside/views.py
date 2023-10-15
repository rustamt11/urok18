from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def admin_index(request):
    products = Product.objects.all()
    return render(request, 'adminside/index.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_index')
    else:
        form = ProductForm()
    return render(request, 'adminside/add_product.html', {'form': form})


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_index')
    else:
        form = ProductForm(instance=product)
    return render(request, 'adminside/edit_product.html', {'form': form})

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('admin_index')
    else:
        form = ProductForm(instance=product)
    return render(request, 'adminside/delete_product.html', {'form': form})
