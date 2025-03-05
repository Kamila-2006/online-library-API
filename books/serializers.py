from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from authors.serializers import AuthorSerializer, AuthorShortSerializer
from .models import Genre, Book


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']

class GenreShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']
        read_only_fields = ['id']

class BookSerializer(serializers.ModelSerializer):
    copies_available = serializers.SerializerMethodField()

    genre = GenreShortSerializer(read_only=True)
    authors = AuthorShortSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'genre', 'isbn', 'published_date', 'description', 'page_count', 'language', 'copies_available']
        read_only_fields = ['id', 'copies_available']

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

    def get_copies_available(self, obj):
        return obj.copies.filter(is_available=True).count()

class BookShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn']