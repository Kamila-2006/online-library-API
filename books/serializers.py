from rest_framework import serializers
from authors.serializers import AuthorSerializer
from .models import Genre, Book


class GenreSerializer(serializers.Serializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']

class BookSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    authors = AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'genre', 'isbn', 'published_date', 'description', 'page_count', 'language']
        read_only_fields = ['id']

    #сделать возможность правильно добавлять жанр и авторов при создании и изменении