from django.shortcuts import render
from .models import Product1


def all_products(request):
    """A view showing all products, including filtered searches"""
    products = Product1.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
