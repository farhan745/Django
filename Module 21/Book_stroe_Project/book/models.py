from django.db import models

# Create your models here.
class BookStore(models.Model):
    category = (
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Science', 'Science'),
        ('History', 'History'),
        ('Biography', 'Biography'),
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=category)
    first_published = models.DateTimeField(auto_now_add=True)  # Date + Time
    last_published = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.book_name
