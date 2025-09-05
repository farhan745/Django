from django.contrib import admin
from .models import BookStore
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'author', 'category', 'first_published', 'last_published')
    search_fields = ('id', 'book_name', 'author', 'category')
admin.site.register(BookStore, BookAdmin)