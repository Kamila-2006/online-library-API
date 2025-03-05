from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from copies.serializers import CopyShortSerializer, BookCopySerializer
from .models import Lending
from datetime import datetime, date


class LendingSerializer(serializers.ModelSerializer):
    book_copy = CopyShortSerializer(read_only=True)
    class Meta:
        model = Lending
        fields = ['id', 'book_copy', 'borrower_name', 'borrower_email', 'borrowed_date', 'due_date', 'returned_date', 'status']
        read_only_fields = ['id', 'borrowed_date', 'book_copy']

class LendingOverdueSerializer(serializers.ModelSerializer):
    book_copy = BookCopySerializer(read_only=True)
    days_overdue = SerializerMethodField()

    class Meta:
        model = Lending
        fields = ['id', 'book_copy', 'borrower_name', 'borrower_email', 'borrowed_date', 'due_date', 'returned_date', 'status', 'days_overdue']

    def get_days_overdue(self, obj):
        if obj.due_date:

            due_date = obj.due_date.date() if isinstance(obj.due_date, datetime) else obj.due_date
            delta = date.today() - due_date
            return max(delta.days, 0)
        return 0