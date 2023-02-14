from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product1

def bag_contents(request):
    """ Context processor """
    
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product1, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    grand_total = total + settings.DELIVERY_CHARGE

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery_charge': settings.DELIVERY_CHARGE,
        'grand_total': grand_total,
    }

    return context