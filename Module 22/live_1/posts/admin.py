from django.contrib import admin
from . import models
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_at', 'update_by')

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)
