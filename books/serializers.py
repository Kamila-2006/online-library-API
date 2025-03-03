from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from authors.serializers import AuthorSerializer
from .models import Genre, Book
from authors.models import Author


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']

class BookSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(
        queryset = Genre.objects.all(),
    )
    authors = serializers.PrimaryKeyRelatedField(
        queryset = Author.objects.all(),
        many = True,
        required = True,
    )
    genre_detail = GenreSerializer(source='genre', read_only=True)
    authors_detail = AuthorSerializer(source='authors', many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'authors_detail', 'genre', 'genre_detail', 'isbn', 'published_date', 'description', 'page_count', 'language']
        read_only_fields = ['id']

    def create(self, validated_data):
        authors = validated_data.pop('authors')
        book = Book.objects.create(**validated_data)
        book.authors.set(authors)
        return book

    def update(self, instance, validated_data):
        authors = validated_data.pop('authors')

        if not authors:
            raise ValidationError({'authors': 'У книги должен быть хотя бы один автор!'})

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.authors.set(authors)
        instance.save()
        return instance

    #добавить счет копий книги