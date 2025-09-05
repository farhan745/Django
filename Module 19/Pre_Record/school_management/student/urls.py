from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('profile/', views.profile,name='student_profile'),
    path('home/', views.home,name='student_home'),
    path('delete/<int:id>/', views.delete_student,name='delete_student'),
]