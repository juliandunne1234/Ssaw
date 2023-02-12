from django.conf import settings

def bag_contents(request):
    """ Context processor """
    
    bag_items = []
    total = 0
    product_count = 0

    grand_total = total + settings.DELIVERY_CHARGE

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery_charge': settings.DELIVERY_CHARGE,
        'grand_total': grand_total,
    }

    return context