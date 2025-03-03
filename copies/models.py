from django.db import models
from books.models import Book


class Copy(models.Model):

    CONDITION_CHOICES = [
        ('new', 'New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='copies')
    inventory_number = models.CharField(max_length=20, unique=True)
    condition = models.CharField(max_length=5, choices=CONDITION_CHOICES, default='new')
    is_available = models.BooleanField(default=True)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} - {self.inventory_number}"