from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'bio', 'birth_date', 'nationality', 'books_count']
        read_only_fields = ['id', 'books_count']

    def get_books_count(self, obj):
        return obj.books.count()