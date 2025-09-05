
from django.contrib import admin
from django.urls import path,include
from . import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",v.tyre_list,name="tyre_list"),
    path("tyre/<int:id>/",v.tyre_details,name="tyre_details"),
    path('tyres/', v.tyres_admin_list, name='tyres_admin_list'),
    path('tyres/create/', v.create_tyre, name='create_tyre'),
    path('tyres/update/<int:id>/', v.update_tyre, name='update_tyre'),
    path('tyres/delete/<int:id>/', v.delete_tyre, name='delete_tyre'),
    
]
