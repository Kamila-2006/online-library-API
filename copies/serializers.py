from rest_framework import serializers
from .models import Copy
from books.serializers import BookSerializer
from books.models import Book


class BookCopySerializer(serializers.ModelSerializer):
    book_id = serializers.PrimaryKeyRelatedField(
        queryset = Book.objects.all(),
        source = 'book',
        write_only = True
    )
    book = BookSerializer(read_only=True)
    class Meta:
        model = Copy
        fields = ['id', 'book', 'book_id' 'inventory_number', 'condition', 'is_available', 'added_date']
        read_only_fields = ['id', 'added_date']