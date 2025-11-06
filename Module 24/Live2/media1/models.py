from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile

from PIL import Image
from io import BytesIO
import os
# Create your models here.
class MediaFile(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='media_files')
    thumbnail = models.ImageField(upload_to='uploads/thumbnails/', blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.thumbnail:
            self.thumbnail = None
        super().save(*args, **kwargs)
    def make_thumbnail(self):
        try:
            img = Image.open(self.file)
            img.thumbnail((300, 300))  # ছোট করে নিলাম

            thumb_name, thumb_extension = os.path.splitext(self.file.name)
            thumb_extension = thumb_extension.lower()
            thumb_filename = f"{thumb_name}_thumb{thumb_extension}"

            image_types = {
                '.jpg': 'JPEG',
                '.jpeg': 'JPEG',
                '.png': 'PNG',
                '.gif': 'GIF'
            }

            if thumb_extension not in image_types:
                return  # unsupported format হলে skip করো

            temp_thumb = BytesIO()
            img.save(temp_thumb, image_types[thumb_extension])
            temp_thumb.seek(0)

            # save thumbnail in storage
            self.thumbnail.save(
                os.path.basename(thumb_filename),
                ContentFile(temp_thumb.read()),
                save=False
            )

            temp_thumb.close()

            super().save(update_fields=['thumbnail'])
        except Exception as e:
            print(f"Error creating thumbnail: {str(e)}")

    class Meta:
        ordering = ['-uploaded_at']
    
