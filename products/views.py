from django.shortcuts import render, get_object_or_404
from .models import Product1


def all_products(request):
    """A view showing all products, including filtered searches"""
    products = Product1.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view showing individual products """
    product = get_object_or_404(Product1, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
