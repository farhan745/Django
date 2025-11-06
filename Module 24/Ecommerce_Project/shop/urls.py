
from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.product_list,name="product-list"),
    path("product/<int:id>/",views.product_detail,name="product-detail"),
    path("cart/",views.cart_detail,name="cart_detail"),
    path("cart/add/<int:id>/",views.cart_add,name="cart_add"),
    path("cart/remove/<int:id>/",views.cart_remove,name="cart_remove"),
    path("checkout/",views.checkout,name="checkout"),
    path("orders/",views.order_history,name="order_history"),
    path("login/",auth_views.LoginView.as_view(template_name="login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(next_page='login'),name="logout"),
    path("signup/",views.signup_view,name="signup"),
    path("product_create/",views.product_create,name="product_create"), 
    path("product_edit/<int:id>/",views.product_update,name="product_edit"),
    path("product_delete/<int:id>/",views.product_delete,name="product_delete"),
    path("category_create/",views.category_create,name="category_create"),

]
