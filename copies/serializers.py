from rest_framework import serializers
from .models import Copy
from books.serializers import BookSerializer


class BookCopySerializer(serializers.ModelSerializer):
    book = BookSerializer()
    class Meta:
        model = Copy
        fields = ['id', 'book', 'inventory_number', 'condition', 'is_available', 'added_date']
        read_only_fields = ['id', 'added_date']

    #добавить book_id