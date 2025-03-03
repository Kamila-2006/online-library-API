from rest_framework import serializers
from authors.serializers import AuthorSerializer
from .models import Genre, Book
from authors.models import Author


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']

class BookSerializer(serializers.ModelSerializer):
    genre_id = serializers.PrimaryKeyRelatedField(
        queryset = Genre.objects.all(),
        source = 'genre',
        write_only = True
    )
    authors_ids = serializers.PrimaryKeyRelatedField(
        queryset = Author.objects.all(),
        source = 'authors',
        many = True,
        write_only = True,
    )
    genre = GenreSerializer(read_only=True)
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'authors_ids', 'genre', 'genre_id', 'isbn', 'published_date', 'description', 'page_count', 'language']
        read_only_fields = ['id']

    #добавить функции чтоб автор создавался и изменялся правильно