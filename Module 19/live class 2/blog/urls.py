from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post_list/', views.post_list,name='post_list'),
    path('post_details/<int:pk>/', views.post_details,name='post_details'),
]
