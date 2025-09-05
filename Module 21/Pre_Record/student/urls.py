from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('create/', views.create_student, name='create_student'),
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('delete/<int:id>/', views.deleteStudent, name='delete_student'),
    path('details/<int:id>/', views.student_details, name='student_detail'),
]
