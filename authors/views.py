from rest_framework import generics
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from .models import Author
from .serializers import AuthorSerializer
from django.shortcuts import get_object_or_404
from books.serializers import BookSerializer
from rest_framework.response import Response


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorBooksView(APIView):
    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        books = author.books.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=HTTP_200_OK)