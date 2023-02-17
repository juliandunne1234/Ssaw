from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from products.models import Product1


def view_bag(request):
    """A view to show the bag contents page"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""

    product = Product1.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        if size in bag[item_id]['items_by_size'].keys():
            bag[item_id]['items_by_size'][size] += quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        bag[item_id] = {'items_by_size': {size: quantity}}
        messages.success(request, f'Added size {size.upper()} {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove item(s) from the shopping bag"""

    try:
        product = Product1.objects.get(pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
