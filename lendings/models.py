from django.db import models
from copies.models import Copy


class Lending(models.Model):

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue'),
    ]

    book_copy = models.ForeignKey(Copy, on_delete=models.CASCADE, related_name='lendings')
    borrower_name = models.CharField(max_length=100)
    borrower_email = models.EmailField()
    borrowed_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    returned_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)