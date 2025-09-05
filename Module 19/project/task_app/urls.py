from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('task_details/<int:id>/', views.task_details, name='task_details'),
]
