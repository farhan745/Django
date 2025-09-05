from django.contrib import admin
from django.urls import path,include
from . import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home,name='home'),
    path('about/',v.about,name='about'),
    path('contact/',v.contact,name='contact'),
    path('reports/',v.reports,name='reports'),
    
    
]