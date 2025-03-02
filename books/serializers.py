from rest_framework import serializers
from authors.serializers import AuthorSerializer
from .models import Book


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(allow_blank=True)

class BookSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    author = AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'genre', 'isbn', 'published_date', 'description', 'page_count', 'language']