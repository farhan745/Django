from django.contrib import admin
from django.urls import path
from . import views as v
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.student_list,name = 'student_list'),
    path('create/', v.student_create,name = 'student_create'),
    path('update/<int:id>/', v.student_update,name = 'student_update'),
    path('delete/<int:pk>/', v.student_delete, name='student_delete'),
    path('detail/<int:pk>/', v.student_detail, name='student_detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)