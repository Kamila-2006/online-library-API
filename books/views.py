from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from copies.serializers import BookCopySerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCopiesView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        copies = book.copies.all()
        serializer = BookCopySerializer(copies, many=True)
        return Response(serializer.data, status=200)