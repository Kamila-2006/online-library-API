from rest_framework import serializers
from .models import Copy
from books.serializers import BookSerializer
from books.models import Book


class BookCopySerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(
        queryset = Book.objects.all(),
        write_only = True
    )
    book_detail = BookSerializer(source='book', read_only=True)
    class Meta:
        model = Copy
        fields = ['id', 'book', 'book_detail', 'inventory_number', 'condition', 'is_available', 'added_date']
        read_only_fields = ['id', 'added_date']