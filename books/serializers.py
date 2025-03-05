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
    copies_available = serializers.SerializerMethodField()

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
        fields = ['id', 'title', 'authors', 'authors_detail', 'genre', 'genre_detail', 'isbn', 'published_date', 'description', 'page_count', 'language', 'copies_available']
        read_only_fields = ['id', 'copies_available', 'genre_detail', 'authors_detail']

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

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if self.context.get('short_version'):
            data.pop('authors_detail', None)
            data.pop('genre_detail', None)
        return data