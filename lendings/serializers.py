from rest_framework import serializers
from copies.serializers import CopyShortSerializer
from .models import Lending


class LendingSerializer(serializers.ModelSerializer):
    book_copy = CopyShortSerializer(read_only=True)
    class Meta:
        model = Lending
        fields = ['id', 'book_copy', 'borrower_name', 'borrower_email', 'borrowed_date', 'due_date', 'returned_date', 'status']
        read_only_fields = ['id', 'borrowed_date', 'book_copy']