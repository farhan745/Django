from django.contrib import admin
from django.urls import path
from . import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.book_list, name='book-list'),
    path('create_book/',v.create_book, name='create_book'),
    path('update_book/<int:id>/',v.update_book, name='update_book'),
    path('delete_book/<int:id>/',v.delete_book, name='delete_book'),
]