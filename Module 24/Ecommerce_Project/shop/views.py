from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Cart, CartItem, Order, OrderItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ProductForm, CategoryForm
from django.db.models import Q


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product created successfully!")
            return redirect('product-list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})
def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('product-detail', id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form, 'product': product})
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.delete()
        return redirect("product-list")
    return redirect("product-detail", id=id)
def product_list(request):
    query = request.GET.get('q')  # search form থেকে query নেওয়া
    products = Product.objects.all()
    categories = Category.objects.all()

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    return render(request, 'product_list.html', {
        'products': products,
        'categories': categories,
        'query': query,  # template-এ পাঠানো
    })

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category created successfully!")
            return redirect('product-list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

@login_required
def cart_add(request, id):
    product = get_object_or_404(Product, id=id)
    cart, _ = Cart.objects.get_or_create(user=request.user)

    # POST থেকে quantity নেওয়া, default 1
    try:
        quantity = int(request.POST.get('quantity', 1))
        if quantity < 1:
            quantity = 1
    except (ValueError, TypeError):
        quantity = 1

    # CartItem get or create
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += quantity  # আগের quantity-এর সাথে যোগ
    else:
        item.quantity = quantity  # নতুন আইটেমের quantity set
    item.save()

    return redirect('cart_detail')
@login_required
def cart_remove(request,id):
    item = get_object_or_404(CartItem,id=id,cart__user=request.user)
    item.delete()
    return redirect('cart_detail')
@login_required
def cart_detail(request):
    cart,_ = Cart.objects.get_or_create(user=request.user)
    return render(request,'cart_detail.html',{'cart':cart})
@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    if cart.items.exists():
        return redirect('product-list')

    order = Order.objects.create(user=request.user, total_price=cart.total_price)
    for item in cart.items.all():
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )
    cart.items.all().delete()  # কার্ট খালি করা
    return render(request, 'checkout_success.html', {'order': order})
@login_required
def order_history(request):
    orders = request.user.orders.all().order_by("-created_at")
    return render(request, "order_history.html", {"orders": orders})
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})