from rest_framework import serializers
from copies.serializers import BookCopySerializer
from .models import Lending
from copies.models import Copy


class LendingSerializer(serializers.ModelSerializer):
    book_copy = serializers.PrimaryKeyRelatedField(
        queryset = Copy.objects.all(),
        write_only = True
    )
    book_copy_detail = BookCopySerializer(source='book_copy', read_only=True)
    class Meta:
        model = Lending
        fields = ['id', 'book_copy', 'book_copy_detail', 'borrower_name', 'borrower_email', 'borrowed_date', 'due_date', 'returned_date', 'status']
        read_only_fields = ['id', 'borrowed_date']

