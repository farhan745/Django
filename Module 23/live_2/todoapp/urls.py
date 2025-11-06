from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello,name='hello'),
    path('hello_protected/',views.hello_protected,name='hello_protected'),
    path('index/',views.index,name='index'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('register/',views.register,name='register'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('tasks/',views.task_list,name='task_list'),
    path('tasks/create/',views.create_task,name='create_task'),
    path('tasks/edit/<int:task_id>/',views.edit_task,name='edit_task'),
    path('tasks/delete/<int:task_id>/',views.delete_task,name='delete_task'),
    
]