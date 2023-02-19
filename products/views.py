from django.shortcuts import render, get_object_or_404
from .models import Product1, Category1
from .forms import ProductForm


def all_products(request):
    """A view showing all products, including filtered searches"""
    products = Product1.objects.all()

    category = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category1.objects.filter(name__in=categories)

    context = {
        'products': products,
        'current_categories': category,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view showing individual products """
    product = get_object_or_404(Product1, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)