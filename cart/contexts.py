
from django.shortcuts import get_object_or_404
from issues.models import Feature


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    for id, quantity in cart.items():
        feature = get_object_or_404(Feature, pk=id)
        total += quantity * feature.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'feature': feature})
        
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count} 

