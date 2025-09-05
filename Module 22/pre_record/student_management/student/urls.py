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
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login_default, name='login'),# eita default username and password diye login er jonno
    path('login_email/', views.user_login_email, name='login_email'),# eita email diye login er jonno
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='user_profile'),
]
