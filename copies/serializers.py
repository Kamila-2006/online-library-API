from rest_framework import serializers
from .models import Copy
from books.serializers import BookShortSerializer
from lendings.models import Lending


class CurrentLendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lending
        fields = ['id', 'borrower_name', 'due_date']
        read_only_fields = ['id', 'borrower_name', 'due_date']

class LendingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lending
        fields = ['id', 'borrower_name', 'borrowed_date', 'returned_date', 'status']

class BookCopySerializer(serializers.ModelSerializer):
    book = BookShortSerializer()

    current_lending = serializers.SerializerMethodField()
    lending_history = serializers.SerializerMethodField()

    class Meta:
        model = Copy
        fields = ['id', 'book', 'inventory_number', 'condition', 'is_available', 'added_date', 'current_lending', 'lending_history']
        read_only_fields = ['id', 'added_date', 'current_lending', 'lending_history']

    def get_current_lending(self, obj):
        lending = Lending.objects.filter(book_copy=obj, status='active').first()
        if lending:
            return CurrentLendingSerializer(lending).data
        return None

    def get_lending_history(self, obj):
        lendings = Lending.objects.filter(book_copy=obj).order_by('-borrowed_date')
        return LendingHistorySerializer(lendings, many=True).data

class CopyShortSerializer(serializers.ModelSerializer):
    book = BookShortSerializer(read_only=True)
    class Meta:
        model = Copy
        fields = ['id', 'book', 'inventory_number']
        read_only_fields = ['id', 'book']
