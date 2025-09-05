from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TaskList, name='task-list'),
    path('create/', views.TaskCreate, name='task-create'),
    path('update/<int:id>/', views.TaskUpdate, name='task-update'),
    path('delete/<int:id>/', views.TaskDelete, name='task-delete'),
    path('detail/<int:id>/', views.TaskDetail, name='task-detail'),
    path('register/', views.RegisterUser, name='register'),
    path('login/', views.LoginUser, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #path('logout/', views.logout_view, name='logout'),
]