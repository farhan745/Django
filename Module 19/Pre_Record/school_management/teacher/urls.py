
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('profile/', views.home,name='teacher_profile'),
]