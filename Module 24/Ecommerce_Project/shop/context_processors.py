from .models import Cart

def cart_count(request):
    if request.user.is_authenticated:
        # latest cart ধরা (বা যেটা active ধরবে)
        cart = Cart.objects.filter(user=request.user).order_by('-created_at').first()
        if cart:
            return {"cart_count": cart.items.count()}
    return {"cart_count": 0}
