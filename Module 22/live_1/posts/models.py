from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_by = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)  # Many-to-Many relationship with Tag

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # related name dile reverly kaj kore. Jemon comment tekhe post hoyar kotha chilo comment.post().related name dile post.comments() hobe
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'