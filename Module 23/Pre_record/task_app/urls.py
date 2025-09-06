from django.contrib import admin
from django.urls import path,include, reverse_lazy
from . import views
from . import forms
from django.contrib.auth.views import PasswordChangeView
# 1. PasswordResetView reset er kaj korte gele eita sobatr aghe ase
from django.contrib.auth.views import PasswordResetView
# 2.PasswordResetConfirmView eta 2nd er kajhe ase
from django.contrib.auth.views import PasswordResetConfirmView
# 3.PasswordResetDoneView eta 3rd er kajhe ase
from django.contrib.auth.views import PasswordResetDoneView
# 4.PasswordResetCompleteView eta last er kajhe ase
from django.contrib.auth.views import PasswordResetCompleteView
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
    path('profile/<str:username>/', views.user_profile, name='user-profile'),
    path(
    'password-change/',
    PasswordChangeView.as_view(
        template_name='password_change.html',
        success_url=reverse_lazy('profile')  # এখানে দিতে হবে
    ),
    name='password_change'
),
    path('password_reset/', PasswordResetView.as_view(template_name='password_reset.html',form_class=forms.PasswordResetForm), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    #path('logout/', views.logout_view, name='logout'),
]